# Flix App — Cliente Streamlit da Flix API

Interface web em [Streamlit](https://streamlit.io/) para consumir a [Flix API](../flix-api/README.md): login com JWT e telas de gêneros, atores, filmes, avaliações e estatísticas. A comunicação com o backend é feita com `requests`, e o token e as listagens ficam em `st.session_state`.

Parte prática do curso [Django-Master PycodeBR](../../README.md).

## Status

Projeto funcional para **listagem e cadastro**. Após o login, o `app.py` monta a navegação com as páginas Início, Atores, Avaliações, Gêneros e Filmes. Não há edição nem exclusão de registros, e as listagens ficam em cache na sessão até o usuário recarregar o login.

## Features

- Tela de login com usuário e senha; `Auth.get_token()` chama `POST {BASE_URL}/auths/token/`
- Token de acesso salvo em `st.session_state.token`; `st.rerun()` após o login
- Navegação lateral com `st.navigation`/`st.Page`
- **Início**: total de filmes, filmes por gênero (gráfico de pizza com Plotly), total de avaliações e média de estrelas
- **Gêneros**: listagem e cadastro
- **Atores**: listagem e cadastro com data de nascimento e nacionalidade
- **Filmes**: listagem e cadastro com gênero e vários atores
- **Avaliações**: listagem e cadastro com filme, estrelas e comentário
- Tabelas com `st_aggrid`
- `actors/country.py` com os 249 países em ISO 3166-1 alpha-2 (nomes em português), compatíveis com o `CountryField` da API
- Listagens cacheadas em `st.session_state` (`genres`, `actors`, `movies`, `reviews`)
- `BASE_URL` carregada do `.env` via `python-dotenv`
- `.env.example` com a variável `BASE_URL` e `config.toml` com o título da aplicação
- Lint com `flake8`/`isort`

## Stack

| Camada | Tecnologia / Versão |
|--------|---------------------|
| Linguagem | Python 3.14.9 |
| UI | Streamlit 1.66.1 |
| Tabelas | streamlit-aggrid 1.2.1.post2 |
| Gráficos | Plotly 7.1.0 + pandas 3.1.0 |
| HTTP | requests 2.34.2 |
| Env | python-dotenv 1.2.4 |
| Backend | Flix API (Django REST + JWT) |
| Lint | flake8 7.4.1, isort 9.0.2 |

Dependências diretas em [`requirements.txt`](requirements.txt); ferramentas de desenvolvimento em [`requirements_dev.txt`](requirements_dev.txt).

## Estrutura

```text
flix-app/
├── app.py                  # entrypoint: login ou navegação autenticada
├── config.toml             # configuração do Streamlit (app_title)
├── api/
│   ├── __init__.py         # carrega .env e expõe BASE_URL
│   └── service.py          # classe Auth (POST /auths/token/)
├── auth/
│   ├── page.py             # render_login()
│   └── service.py          # login() e logout()
├── home/
│   └── page.py             # estatísticas de filmes
├── genres/
│   ├── page.py             # listagem e cadastro
│   ├── repository.py       # GenreRepository (get/create)
│   └── service.py          # GenreService (cache em session_state)
├── actors/
│   ├── country.py          # países ISO alpha-2 para o selectbox
│   ├── page.py             # listagem e cadastro
│   ├── repository.py       # ActorRepository (get/create)
│   └── service.py          # ActorService (cache em session_state)
├── movies/
│   ├── page.py             # listagem e cadastro
│   ├── repository.py       # MovieRepository (get/create/stats)
│   └── service.py          # MovieService (cache em session_state)
├── reviews/
│   ├── page.py             # listagem e cadastro
│   ├── repository.py       # ReviewRepository (get/create)
│   └── service.py          # ReviewService (cache em session_state)
├── .env.example            # modelo de configuração (BASE_URL)
├── .env                    # configuração local (ignorado pelo git)
├── .flake8                 # exclui venv e define limite de 89 colunas
├── requirements.txt
└── requirements_dev.txt
```

Não há `pyproject.toml` nem testes automatizados; o `config.toml` só define o título da aplicação.

## Integração com a Flix API

### Configuração

Copie `projetos/flix-app/.env.example` para `.env` e ajuste a URL base da API, **sem barra no final**:

```dotenv
BASE_URL='http://127.0.0.1:8000/api/v1'
```

`api/__init__.py` chama `load_dotenv('.env')` e expõe `BASE_URL = os.getenv('BASE_URL')`. Por isso, execute o Streamlit a partir da pasta `flix-app`; caso contrário o `.env` não será encontrado.

### Endpoints usados

Todas as rotas exigem `Authorization: Bearer <access>`, exceto o login.

| Ação | Método e rota | Corpo |
|------|---------------|-------|
| Login | `POST {BASE_URL}/auths/token/` | form `username`, `password`; retorna `access` e `refresh` |
| Listar gêneros | `GET {BASE_URL}/genres/` | — |
| Criar gênero | `POST {BASE_URL}/genres/` | `name` |
| Listar atores | `GET {BASE_URL}/actors/` | — |
| Criar ator | `POST {BASE_URL}/actors/` | `name`, `birthday`, `nationality` |
| Listar filmes | `GET {BASE_URL}/movies/` | — |
| Criar filme | `POST {BASE_URL}/movies/` | `title`, `sinopse`, `release_date`, `genre`, `actors` |
| Estatísticas | `GET {BASE_URL}/movies/stats/` | — (retorna `total_movies`, `movies_by_genre`, `total_reviews`, `average_stars`) |
| Listar avaliações | `GET {BASE_URL}/reviews/` | — |
| Criar avaliação | `POST {BASE_URL}/reviews/` | `movie`, `stars`, `comment` |

O login só valida as credenciais. As rotas de CRUD da Flix API também exigem as permissões Django do usuário (`genres.view_genre`, `actors.add_actor`, `movies.view_movie`, etc.); superusuários passam em tudo. Detalhes em [`../flix-api/README.md`](../flix-api/README.md).

## Quickstart

1. Suba a Flix API seguindo o [README do backend](../flix-api/README.md) (por padrão em `http://127.0.0.1:8000`).
2. Prepare o cliente:

```bash
cd projetos/flix-app

# Ambiente (o venv local já existe no repositório de estudo)
python -m venv venv
source venv/bin/activate

# Dependências
pip install -r requirements.txt

# Configuração
cp .env.example .env
# edite BASE_URL para a URL da API

# Rodar a interface
streamlit run app.py
```

Acesse `http://localhost:8501`, informe usuário e senha de um superusuário (ou de um usuário com as permissões necessárias) e faça login. A primeira página exibida é **Início**, com as estatísticas de filmes.

Para usar a API publicada, basta trocar o `BASE_URL` no `.env` (o ambiente local atual aponta para uma instância no PythonAnywhere).

### Lint

```bash
cd projetos/flix-app
./venv/bin/flake8 .
./venv/bin/isort --check-only .
```

## Limitações conhecidas

- `auth/service.py`: `logout()` usa `st.session_state.key()`, que não existe (o correto é `keys()`); qualquer resposta `401` termina em `AttributeError` em vez de voltar ao login.
- `actors/page.py`: se “Salvar” for clicado sem selecionar nacionalidade, `nationality_names[None]` gera `KeyError`.
- O `ActorSerializer` da Flix API expõe apenas `id` e `name`; `birthday` e `nationality` são enviados, mas descartados pelo backend.
- `movies/page.py` e `reviews/page.py`: com o banco vazio, `st.selectbox(options=[])` retorna `None` e o clique em “Salvar” gera `KeyError`; se as listas vierem `None` após um `401`, os `for`/dict comprehensions quebram com `TypeError`.
- A resposta de criação de filme/avaliação usa IDs (`genre`, `actors`, `movie`), enquanto a listagem usa objetos aninhados. O grid pode levantar `KeyError` no primeiro filme/avaliação ou misturar os dois formatos.
- As listagens em `session_state` não são invalidadas; alterações feitas por outra sessão não aparecem até novo login.
- Só o `access` é guardado; não há refresh automático nem expiração de sessão.
- As requisições não têm `timeout` e só tratam `401`; `400`, `403` e `500` viram uma `Exception` genérica com traceback na tela.
- `Auth.get_token()` trata qualquer status diferente de `200` como “Usuário ou senha inválidos” e devolve `status_code` como `set`.
- O login não valida campos vazios e o `spinner` não é usado como context manager.
- Não há edição nem exclusão de registros nas telas.
- Sem testes automatizados.

Próximos passos sugeridos: corrigir o logout, tratar listas vazias e respostas `400`/`403`, padronizar o formato dos dados no grid, adicionar refresh/expiração do JWT, timeouts, edição/exclusão e testes.

## Licença

MIT — ver [../../LICENSE](../../LICENSE).
