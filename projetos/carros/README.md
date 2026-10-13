# Carros — CRUD Concessionária Django + IA Gemini

Monolito Django MVT para cadastro e vitrine de carros: CRUD com upload de imagem, busca por nome, autenticação (login/registro), admin em PT-BR, inventário automático via signals e cliente Google Gemini para geração de descrições comerciais.

Parte prática do curso [Django-Master PycodeBR](../../README.md).

## Features

- CRUD de carros (marca, nome, placa, anos de fabricação/modelo, preço, descrição, imagem, ativo)
- Listagem pública com busca `?search=` e cards com imagem fallback
- Detalhamento público com preço, placa, anos e descrição
- Criação, edição e exclusão restritas a usuários autenticados (`login_required`)
- Autenticação com `User` padrão: login, logout, registro (`UserCreationForm` / `AuthenticationForm`)
- Upload de imagens (`ImageField upload_to='cars/'`), servidas em `MEDIA_URL` no modo `DEBUG`
- Inventário automático: cada `save`/`delete` de `Car` cria snapshot em `CarInventory` (quantidade + valor total)
- Limpeza automática de arquivos de imagem antigos (troca e exclusão)
- Descrição automática placeholder no `pre_save` quando vazia; integração Gemini pronta mas desativada (linha comentada)
- Admin configurado para `Brand` e `Car` com busca e listagem
- i18n `pt-br`, timezone `America/Sao_Paulo`

## Stack

| Camada | Tecnologia / Versão |
|--------|---------------------|
| Framework | Django 6.1.2 |
| Linguagem | Python 3.14 (venv incluso no projeto) |
| Banco dev | SQLite (`db.sqlite3`) |
| Banco prod | PostgreSQL (bloco comentado em `settings.py`, via env) |
| Imagens | Pillow 12.3.0 |
| Env | python-dotenv 1.2.4 |
| IA | google-genai 2.29.0 (modelo `gemini-3.8-flash`) |
| Frontend | Templates Django + Bootstrap 5.3.8 CDN, CSS próprio `static/css/base.css` |
| Auth | `django.contrib.auth` (sem custom user) |

Dependências completas em [`requirements.txt`](requirements.txt).

## Arquitetura e estrutura

```text
carros/
├── manage.py
├── core/                   # config do projeto
│   ├── settings.py
│   ├── urls.py             # admin/ + accounts/ + cars/ + media em DEBUG
│   ├── model.py            # BaseModel abstrato
│   └── wsgi.py / asgi.py
├── apps/
│   ├── cars/               # domínio principal
│   │   ├── models.py       # Brand, Car, CarInventory
│   │   ├── views.py        # 5 CBVs
│   │   ├── urls.py         # app_name='cars'
│   │   ├── forms.py        # CarForm
│   │   ├── signals.py      # inventário + cleanup + desc automática
│   │   ├── admin.py
│   │   ├── apps.py         # CarsConfig.ready() importa signals
│   │   └── migrations/0001_initial, 0002_carinventory, 0003_car_desc
│   └── accounts/           # autenticação
│       ├── views.py        # FBVs login_view, logout_view, register_view
│       ├── urls.py         # app_name='accounts'
│       └── models.py / admin.py / tests.py (vazios, usa auth.User)
├── ia_api/
│   └── client.py           # generate(prompt) -> str
├── templates/
│   ├── base.html           # navbar, busca, Bootstrap, blocks title/content
│   ├── cars/list.html, detail.html, new.html, update.html, delete.html
│   ├── accounts/login.html, register.html
│   └── includes/forms/input.html (vazio)
├── static/
│   ├── css/base.css
│   ├── img/avatar.png, default-car.png
│   └── js/ (vazio)
├── media/cars/             # uploads (ignorado pelo git)
├── db.sqlite3
├── requirements.txt
├── .env / .env-example
└── README.md
```

Padrão: monolito server-rendered, sem API REST, sem AJAX. Templates centralizados em `BASE_DIR/templates` com `APP_DIRS=True`. Estáticos em `BASE_DIR/static`.

## Modelos

Todos herdam `BaseModel` (`core/model.py`): `created_at` (auto_now_add), `updated_at` (auto_now), `is_active` (default True). `ordering = ['-created_at']`.

| Modelo | Campos | Observações |
|--------|--------|-------------|
| `Brand` | `name Char(255, unique)` | `Marca` / `Marcas` |
| `Car` | `name Char(255)`, `desc Text(blank,null)`, `plate Char(10, unique, blank,null)`, `image ImageField(upload_to='cars/', blank,null)`, `factory_year PositiveInt(blank,null)`, `model_year PositiveInt(blank,null)`, `price Decimal(10,2, blank,null)`, `brand FK(Brand, PROTECT, related_name='brands')` | `Carro` / `Carros`. `PROTECT` impede apagar marca com carros. `related_name='brands'` retorna carros a partir da marca (nomenclatura invertida, o ideal seria `cars`) |
| `CarInventory` | `amount PositiveInt(default=0)`, `value Decimal(10,2)` | `Estoque` / `Estoque de Carros`. Sem FK: cada save/delete cria uma nova linha snapshot, não atualiza. Tabela cresce de forma append-only |

Migrations: `0001_initial` (Brand + Car sem desc), `0002_carinventory`, `0003_car_desc`.

## Rotas

Base (`core/urls.py`): sem rota `/` raiz. Acesso direto em `/cars/` e `/admin/`. Mídia servida apenas se `DEBUG`.

### Cars (`app_name='cars'`, prefixo `cars/`)

| Método | Rota | View | Nome | Auth |
|--------|------|------|------|------|
| GET | `/cars/` | `ListViewCar` | `list_car` | pública (`?search=` filtra `name__icontains` + `is_active=True`) |
| GET/POST | `/cars/new` | `CreateViewCar` | `new_car` | login |
| GET | `/cars/detail/<int:pk>/` | `DetailViewCar` | `detail_car` | pública |
| GET/POST | `/cars/update/<int:pk>/` | `UpdateViewCar` | `update_car` | login (volta para detail) |
| GET/POST | `/cars/delete/<int:pk>/` | `DeleteViewCar` | `delete_car` | login |

### Accounts (`app_name='accounts'`, prefixo `accounts/`)

| Rota | View | Nome |
|------|------|------|
| `accounts/login` | `login_view` (FBV, `authenticate` + `login`, erro via `AuthenticationForm`) | `login_view` |
| `accounts/logout` | `logout_view` (FBV, `logout` + redirect login) | `logout_view` |
| `accounts/register` | `register_view` (FBV, `UserCreationForm`, sem auto-login) | `register_view` |

Sem `password_reset` / `password_change`, sem trailing slash, sem controle por objeto (qualquer logado edita qualquer carro).

## Views, forms, signals e IA

### Views (`apps/cars/views.py`, `apps/accounts/views.py`)

- `ListViewCar(ListView)`: `model=Car`, `template='cars/list.html'`, `context='cars'`, `get_queryset()` com `is_active` + busca.
- `DetailViewCar(DetailView)`: `template='cars/detail.html'`, contexto padrão `object`.
- `CreateViewCar(CreateView)`: `form_class=CarForm`, `template='cars/new.html'`, `success_url='/cars/'` (hardcoded).
- `UpdateViewCar(UpdateView)`: `template='cars/update.html'`, `get_success_url()` para `cars:detail_car`.
- `DeleteViewCar(DeleteView)`: `template='cars/delete.html'`, `success_url='/cars/'`.
- Proteção via `@method_decorator(login_required(login_url='accounts:login_view'), name='dispatch')` (não usa `LoginRequiredMixin`).
- Accounts 100% FBV conforme tabela acima. Logout aceita GET.

### Forms (`apps/cars/forms.py`)

`CarForm(ModelForm, fields='__all__')`: `brand` com classe Bootstrap `form-select`, `clean_price()` rejeita valor negativo (`add_error`). Sem validação extra de anos/placa. Templates `new`/`update` usam inputs HTML manuais + `{{ form.brand }}` + `{{ form.errors }}`, não `{{ form.as_p }}`.

### Signals (`apps/cars/signals.py`, registrado em `CarsConfig.ready()`)

- `update_inventory()`: `count()` + `Sum('price')` dos ativos → `CarInventory.objects.create(amount, value)`. O `Sum('id')` agregado como `total_amount` é calculado e ignorado.
- `post_save` e `post_delete` de `Car` chamam `update_inventory()`.
- `post_delete` remove o arquivo físico da imagem, se existir.
- `pre_save`: se for update e a imagem trocou, remove o arquivo antigo; se `desc` vazia, define `'Descrição gerada automaticamente...'` (linha IA comentada abaixo).

### IA (`ia_api/client.py`)

`generate(prompt: str) -> str`: cria `genai.Client(api_key=settings.GEMINI_API_KEY)`, chama `models.generate_content(model='gemini-3.8-flash', contents='Crie uma descrição comercial ... até 500 caracteres ...', config={'max_output_tokens': 500, 'temperature': 0.4})`, faz `strip`, valida vazio, trunca em 500 chars, com retry 3x (`sleep 2**attempt`) apenas para `errors.ServerError`.

Status: código pronto, mas não chamado (`signals.py:49` comentado). Se reativado, roda de forma síncrona no `pre_save` (adiciona latência ao save).

## Templates e estáticos

- `base.html`: `{% load static %}`, Bootstrap 5.3.8 CSS+JS CDN, `css/base.css`, navbar dark com `Início`, `Cadastrar` (se autenticado), busca GET `?search`, dropdown avatar `Olá, user + Logout` ou botão `Login`. Blocos `title` e `content`.
- `cars/list.html`: grid de cards, `default-car.png` quando sem imagem, marca+nome, anos, preço ou `R$0,00`, `{% empty %}` com alerta. Atenção: o teste atual `{% if car.image.url is not None %}` levanta `ValueError` quando não há arquivo; o correto é `{% if car.image %}`.
- `cars/detail.html`: 2 colunas, imagem, marca/nome/anos/placa/preço/desc, botões Editar/Deletar se autenticado.
- `cars/new.html` / `update.html`: form `multipart` + CSRF, inputs manuais, `is_active` como switch, `image` file.
- `cars/delete.html`: confirmação.
- `accounts/login.html` e `register.html`: forms manuais com `non_field_errors` / `form.errors`.
- `static/css/base.css`: remove underline de links, `.avatar-img` 40px, `.card-img-car` 100%x280px, `.card-img-car-form` 100%x400px.

## Configuração (.env)

Copie `.env-example` para `.env`. Variáveis (`core/settings.py`):

| Var | Exemplo | Uso |
|-----|---------|-----|
| `SECRET_KEY` | `your-secret-key-here` | obrigatório, sem fallback (quebra se ausente) |
| `DEBUG` | `0` | `bool(os.getenv('DEBUG','1'))` — atenção: `bool('0')` é `True` em Python, então `DEBUG=0` não desliga o debug. Correção sugerida: `os.getenv('DEBUG') == '1'` |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | `os.getenv(...).split(',')` — quebra se var ausente |
| `GEMINI_API_KEY` | `your-key-api-here` | consumida por `ia_api/client.py` |
| `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` | ver `.env-example` | usados apenas se ativar o bloco Postgres |

Email usa chave `MAILERS` com `console.EmailBackend`, que não é o padrão Django (`EMAIL_BACKEND`) e hoje é inócua.

## Quickstart

```bash
cd projetos/carros

# 1. Ambiente
python -m venv venv
source venv/bin/activate

# 2. Dependências
pip install -r requirements.txt

# 3. Env
cp .env-example .env
# edite SECRET_KEY, DEBUG, ALLOWED_HOSTS, GEMINI_API_KEY

# 4. Banco
python manage.py migrate

# 5. Admin
python manage.py createsuperuser

# 6. Rodar
python manage.py runserver
```

Acesse:

- Vitrine: `http://127.0.0.1:8000/cars/`
- Novo carro: `http://127.0.0.1:8000/cars/new` (requer login)
- Admin: `http://127.0.0.1:8000/admin/`
- Login: `http://127.0.0.1:8000/accounts/login`
- Registro: `http://127.0.0.1:8000/accounts/register`

## PostgreSQL (produção)

Em `core/settings.py` o bloco SQLite está ativo e o Postgres comentado. Para trocar, comente o bloco SQLite e descomente:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST", 'localhost'),
        'PORT': os.getenv("DB_PORT", 5432),
    }
}
```

Requer driver `psycopg` (não listado em `requirements.txt`) e as vars `DB_*` no `.env`. Depois rode `python manage.py migrate`.

## Comandos úteis

```bash
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver
python manage.py shell
python manage.py collectstatic  # STATIC_ROOT está comentado em settings.py
```

## Limitações conhecidas

- `DEBUG` via `bool()` sempre True; `ALLOWED_HOSTS` frágil sem `.env`; `SECRET_KEY` sem fallback.
- `MAILERS` deveria ser `EMAIL_BACKEND`.
- `related_name='brands'` confuso (retorna carros).
- `CarInventory` append-only, sem admin e sem limpeza; `Sum('id')` morto.
- `{% if car.image.url is not None %}` quebra sem imagem; usar `{% if car.image %}`.
- Logout via GET; `success_url='/cars/'` hardcoded em Create/Delete.
- `includes/forms/input.html`, `static/js/`, `tests.py` vazios.
- IA pronta mas desativada; se ativada, sem fila (bloqueia request).

Próximos passos sugeridos: corrigir `DEBUG`/`ALLOWED_HOSTS`, registrar `CarInventory` no admin com rotina de limpeza, trocar `related_name`, corrigir teste de imagem, exigir POST no logout, cobrir models/views/signals com testes, reativar Gemini de forma assíncrona.

## Licença

MIT — ver [../../LICENSE](../../LICENSE).
