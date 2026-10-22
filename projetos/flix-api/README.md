# Flix API — Catálogo de Filmes (Django REST)

API REST para catálogo de filmes, com atores, gêneros e avaliações. Usa Django REST Framework (DRF), autenticação JWT com SimpleJWT, permissões por modelo do Django, serializers aninhados para leitura, estatísticas agregadas e documentação OpenAPI (Swagger/Redoc). Todos os recursos ficam sob `/api/v1/`.

Parte prática do curso [Django-Master PycodeBR](../../README.md).

## Features

- CRUD REST de gêneros, atores, filmes e avaliações
- Leitura com serializers aninhados: filme traz gênero/atores; avaliação traz o filme completo
- Escrita separada da leitura via `ModelSerializer` (`fields = '__all__'`)
- Média de estrelas por filme no campo `rate` (`Avg('stars')`)
- Endpoint de estatísticas gerais (`/movies/stats/`)
- Autenticação JWT: `token/`, `token/refresh/`, `token/verify/`
- Autorização por permissões nativas do Django (`app_label.action_model`) em todas as views de CRUD
- Admin em PT-BR para todos os modelos
- Documentação OpenAPI: schema, Swagger UI e Redoc
- Importação de atores via CSV (`import_actors`) com `bulk_create`
- `BaseModel` abstrato com `created_at`, `updated_at` e `is_active`; listagens filtram `is_active=True`
- Nacionalidade com `django-countries` (ISO alpha-2)
- i18n `pt-BR`, timezone `America/Sao_Paulo`

## Stack

| Camada | Tecnologia / Versão |
|--------|---------------------|
| Framework | Django 6.1.2 |
| Linguagem | Python 3.14 (venv local no projeto) |
| API | DRF 3.18.3 |
| Auth | SimpleJWT 5.5.1 (access 7 dias, refresh 30 dias) |
| Documentação | drf-spectacular 0.30.0 |
| Países | django-countries 9.1.0 |
| Banco dev | SQLite (`db.sqlite3`) |
| Banco prod | PostgreSQL não configurado (apenas `psycopg2-binary` listado) |
| Admin | `django.contrib.admin` |

Dependências completas em [`requirements.txt`](requirements.txt); ferramentas de lint em [`requirements_dev.txt`](requirements_dev.txt).

## Arquitetura e estrutura

```text
flix-api/
├── manage.py
├── core/
│   ├── settings.py         # DRF, JWT, spectacular, i18n
│   ├── urls.py             # admin + api/v1 + schema
│   ├── models.py           # BaseModel abstrato
│   ├── permissions.py      # CustomPermissions
│   └── wsgi.py / asgi.py
├── apps/
│   ├── auths/              # só urls.py com TokenObtain/Refresh/Verify
│   ├── actors/
│   │   ├── models.py       # Actor
│   │   ├── serializers.py  # ActorSerializer
│   │   ├── views.py        # ListCreate + RetrieveUpdateDestroy
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── management/commands/import_actors.py
│   ├── genres/
│   │   ├── models.py       # Genre
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── movies/
│   │   ├── models.py       # Movie
│   │   ├── serializers.py  # MovieSerializer (leitura) + MovieModelSerializer (escrita)
│   │   ├── views.py        # CRUD + MovieStatsView
│   │   ├── urls.py
│   │   └── admin.py
│   └── reviews/
│       ├── models.py       # Review
│       ├── serializers.py  # ReviewSerializer (leitura) + ReviewModelSerializer (escrita)
│       ├── views.py
│       ├── urls.py
│       └── admin.py
├── static/actors.csv       # massa de exemplo (atores)
├── requirements.txt
├── requirements_dev.txt
├── .env-example
└── README.md
```

Não há templates nem front-end: o projeto é somente API + admin. Não existe rota `/`.

## Modelos

Todos herdam `core.models.BaseModel` (`created_at`, `updated_at`, `is_active`; tabela abstrata).

| Modelo | Campos | Observações |
|--------|--------|-------------|
| `Actor` | `name Char(200)`, `birthday Date(blank,null)`, `nationality CountryField(blank,null)` | `ordering=['name']`. Nacionalidade em ISO alpha-2 (`BR`, `US`, ...) |
| `Genre` | `name Char(200)` | `ordering=['id']` |
| `Movie` | `title Char(500)`, `sinopse Text(blank,null)`, `genre FK(Genre, PROTECT, related_name='movies')`, `release_date Date(blank,null)`, `actors M2M(Actor, related_name='movies')` | `ordering=['-created_at']` |
| `Review` | `movie FK(Movie, PROTECT, related_name='reviews')`, `stars PositiveInt` (validators 0–5), `comment Text(blank,null)` | `ordering=['-created_at']`. Sem FK de usuário e sem unicidade por filme |

- `PROTECT` impede excluir um gênero com filmes ou um filme com avaliações. A exclusão é física (hard delete); `is_active` é apenas filtro de listagem, não soft delete.
- `Review` não guarda o autor; qualquer usuário autorizado pode criar/editar/apagar qualquer avaliação. Não há restrição de uma avaliação por filme.
- Migrations: `actors/0001` + `0002` (nacionalidade vira `CountryField`); `genres/0001` + `0002` (ordering); `movies/0001`; `reviews/0001`.

## Rotas

Base: `/admin/`, `/api/v1/` e `/api/v1/schema/`. Todas as rotas de CRUD exigem JWT válido (exceto schema e token).

### Autenticação (`apps/auths/urls.py`, prefixo `api/v1/auths/`)

| Método | Rota | View | Nome |
|--------|------|------|------|
| POST | `/api/v1/auths/token/` | `TokenObtainPairView` | `token_obtain_pair` |
| POST | `/api/v1/auths/token/refresh/` | `TokenRefreshView` | `token_refresh` |
| POST | `/api/v1/auths/token/verify/` | `TokenVerifyView` | `token_verify` |

### Gêneros (`prefixo api/v1/genres/`)

| Método | Rota | View | Nome |
|--------|------|------|------|
| GET/POST | `/api/v1/genres/` | `GenreListCreateAPIView` | `view_genres` |
| GET/PUT/PATCH/DELETE | `/api/v1/genres/<pk>/` | `GenreRetrieveUpdateDestroyAPIView` | `detail_genres` |

### Atores (`prefixo api/v1/actors/`)

| Método | Rota | View | Nome |
|--------|------|------|------|
| GET/POST | `/api/v1/actors/` | `ActorListCreateAPIView` | `view_actors` |
| GET/PUT/PATCH/DELETE | `/api/v1/actors/<pk>/` | `ActorRetrieveUpdateDestroyAPIView` | `detail_actors` |

### Filmes (`prefixo api/v1/movies/`)

| Método | Rota | View | Nome |
|--------|------|------|------|
| GET/POST | `/api/v1/movies/` | `MovieListCreateAPIView` | `movie_view` |
| GET/PUT/PATCH/DELETE | `/api/v1/movies/<pk>/` | `MovieRetrieveUpdateDestroyAPIView` | `movie_detail` |
| GET | `/api/v1/movies/stats/` | `MovieStatsView` | `movie_stats` |

### Avaliações (`prefixo api/v1/reviews/`)

| Método | Rota | View | Nome |
|--------|------|------|------|
| GET/POST | `/api/v1/reviews/` | `ReviewListCreateAPIView` | `review_view` |
| GET/PUT/PATCH/DELETE | `/api/v1/reviews/<pk>/` | `ReviewRetrieveUpdateDestroyAPIView` | `review_detail` |

### Documentação

| Método | Rota | View | Nome |
|--------|------|------|------|
| GET | `/api/v1/schema/` | `SpectacularAPIView` | `schema` |
| GET | `/api/v1/schema/swagger-ui/` | `SpectacularSwaggerView` | `swagger-ui` |
| GET | `/api/v1/schema/redoc/` | `SpectacularRedocView` | `redoc` |

## Autenticação e permissões

Toda view de CRUD usa `permission_classes = (IsAuthenticated, CustomPermissions,)`. `CustomPermissions` (`core/permissions.py`) monta a permissão a partir do modelo do `queryset` da view e do método HTTP:

| Método | Permissão exigida |
|--------|-------------------|
| `GET`, `HEAD`, `OPTIONS` | `app_label.view_model` |
| `POST` | `app_label.add_model` |
| `PUT`, `PATCH` | `app_label.change_model` |
| `DELETE` | `app_label.delete_model` |

Ou seja: além de estar autenticado, o usuário precisa das permissões do Django para o modelo (ex.: `movies.add_movie`). Superusers passam em tudo. O endpoint `/movies/stats/` usa `queryset = Movie...`, logo exige `movies.view_movie`.

Fluxo básico:

```bash
# 1. Obter o par access/refresh
curl -X POST http://127.0.0.1:8000/api/v1/auths/token/ \
  -H 'Content-Type: application/json' \
  -d '{"username": "admin", "password": "sua-senha"}'

# 2. Usar o access nas chamadas
curl http://127.0.0.1:8000/api/v1/movies/ \
  -H 'Authorization: Bearer <access_token>'
```

Configuração JWT (`SIMPLE_JWT`): access de 7 dias, refresh de 30 dias, sem rotação/blacklist.

## Serializers e payloads

- `ActorSerializer` e `GenreSerializer`: `['id', 'name']` para leitura **e** escrita. Assim, `birthday`, `nationality` e `is_active` não são editáveis pela API; use o admin ou a importação CSV para atores.
- `MovieSerializer` (GET): `id`, `rate`, `title`, `sinopse`, `genre` (aninhado `{id, name}`), `actors` (lista aninhada), `release_date`.
  - `rate` é a média de `stars` arredondada em 1 casa ou a string `"Sem Avaliação"` quando não há reviews (tipo inconsistente).
- `MovieModelSerializer` (POST/PUT/PATCH): `fields = '__all__'`; `genre` e `actors` são IDs. `validate_sinopse()` limita a 500 caracteres na API, embora o modelo aceite mais.
- `ReviewSerializer` (GET): `id`, `stars`, `comment`, `movie` (filme completo e aninhado, com gênero, atores e `rate`).
- `ReviewModelSerializer` (POST/PUT/PATCH): `fields = '__all__'`; `movie` é ID.
- A resposta de um POST/PUT/PATCH usa o serializer de escrita, não o de leitura.
- Não há paginação configurada: listagens retornam todos os registros ativos. Também não há filtros de busca/ordenação por query string; os querysets só aplicam `is_active=True`.

## Estatísticas (`GET /api/v1/movies/stats/`)

Resposta calculada em `MovieStatsView`:

```json
{
  "total_movies": 10,
  "movies_by_genre": [
    {"genre__name": "Ação", "count": 4}
  ],
  "total_reviews": 25,
  "average_stars": 3.8
}
```

- `total_movies` e `movies_by_genre` consideram apenas filmes ativos.
- `total_reviews` e `average_stars` contam **todas** as avaliações, inclusive de filmes inativos e avaliações com `is_active=False`.
- `average_stars` é `0` quando não há avaliações.

## Admin e importação de atores

O admin registra `Actor`, `Genre`, `Movie` e `Review` com `list_display` e `search_fields`.

O comando `import_actors` lê um CSV com cabeçalho `name,birthday,nationality`:

```bash
./venv/bin/python manage.py import_actors static/actors.csv
```

- `birthday` deve estar em `YYYY-MM-DD`; `nationality` em ISO alpha-2 (`BR`, `US`, `GB`, ...).
- Usa `bulk_create`: não faz deduplicação nem update. Rodar o mesmo arquivo duas vezes duplica os atores.
- Só `ImportError` e `FileNotFoundError` são tratados; data inválida ou campo ausente propaga `ValueError`/`KeyError` e aborta o comando.
- O arquivo de exemplo `static/actors.csv` já vem no repositório.

## Configuração (.env)

Copie `.env-example` para `.env`. Variáveis usadas por `core/settings.py`:

| Var | Exemplo | Uso |
|-----|---------|-----|
| `SECRET_KEY` | `your-secret-key-here` | obrigatória, sem fallback (quebra se ausente) |
| `DEBUG` | `1` | `bool(os.getenv('DEBUG','1'))` — atenção: `bool('0')` é `True`, então `DEBUG=0` não desliga o debug. Correção sugerida: `os.getenv('DEBUG') == '1'` |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | `os.getenv(...).split(',')` — quebra se a variável estiver ausente |

Não há variáveis de banco: o SQLite é fixo em `BASE_DIR / 'db.sqlite3'`. A chave `MAILERS` existe com `console.EmailBackend`, mas o padrão Django é `EMAIL_BACKEND`, então ela é inócua.

Arquivos estáticos usam `STATIC_URL = 'static/'`, `STATIC_ROOT = BASE_DIR / 'staticfiles'` (destino do `collectstatic`) e `STATICFILES_DIRS = [BASE_DIR / 'static']` (origem, onde fica `actors.csv`).

## Quickstart

```bash
cd projetos/flix-api

# 1. Ambiente
python -m venv venv
source venv/bin/activate

# 2. Dependências
pip install -r requirements.txt

# 3. Env
cp .env-example .env
# edite SECRET_KEY, DEBUG e ALLOWED_HOSTS

# 4. Banco
python manage.py migrate

# 5. Admin (superuser passa nas permissões)
python manage.py createsuperuser

# 6. Rodar
python manage.py runserver
```

Acesse:

- Admin: `http://127.0.0.1:8000/admin/`
- Swagger: `http://127.0.0.1:8000/api/v1/schema/swagger-ui/`
- Redoc: `http://127.0.0.1:8000/api/v1/schema/redoc/`
- Schema OpenAPI: `http://127.0.0.1:8000/api/v1/schema/`
- Token JWT: `POST http://127.0.0.1:8000/api/v1/auths/token/`

No Swagger, o esquema de segurança é declarado como `apiKey` no header `Authorization`; informe o valor completo `Bearer <access_token>`.

## Comandos úteis

```bash
./venv/bin/python manage.py check
./venv/bin/python manage.py makemigrations --check --dry-run
./venv/bin/python manage.py migrate
./venv/bin/python manage.py createsuperuser
./venv/bin/python manage.py runserver
./venv/bin/python manage.py import_actors static/actors.csv
./venv/bin/flake8 .
./venv/bin/isort --check-only .
```

## Limitações conhecidas

- `DEBUG` via `bool()` sempre `True`; `ALLOWED_HOSTS` frágil sem `.env`; `SECRET_KEY` sem fallback.
- `MAILERS` deveria ser `EMAIL_BACKEND`.
- `ActorSerializer` e `GenreSerializer` expõem apenas `id`/`name`: `birthday`, `nationality` e `is_active` não são editáveis pela API.
- `rate` alterna entre número e string; `Review` não tem autor nem unicidade por filme.
- Hard delete com `PROTECT`: excluir gênero/filme referenciado levanta `ProtectedError` (tende a virar erro 500 na API).
- Sem paginação, busca, filtros ou ordenação configurados; listagens retornam todos os ativos.
- Serializers aninhados não usam `select_related`/`prefetch_related` (risco de N+1).
- Estatísticas misturam escopos (filmes ativos vs. todas as avaliações).
- `import_actors` duplica registros se reexecutado e não trata CSV inválido.
- Sem testes automatizados.
- `flake8` acusa `E501` pré-existente em `apps/reviews/views.py:23` (linha com 80 colunas); `isort` passa.

Próximos passos sugeridos: corrigir `DEBUG`/`ALLOWED_HOSTS`, ampliar os serializers de ator/gênero, normalizar o tipo de `rate`, adicionar paginação/filtros, proteger a exclusão com tratamento de `ProtectedError`, usar `select_related`/`prefetch_related`, tornar a importação idempotente e cobrir views/permissões com testes.

## Licença

MIT — ver [../../LICENSE](../../LICENSE).
