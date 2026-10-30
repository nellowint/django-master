# Flix App — Cliente Streamlit da Flix API

Interface web em [Streamlit](https://streamlit.io/) para consumir a [Flix API](../flix-api/README.md): login com JWT e, nas próximas etapas, CRUD de gêneros, filmes, atores e avaliações. A comunicação com o backend é feita com `requests`, e o token fica em `st.session_state`.

Parte prática do curso [Django-Master PycodeBR](../../README.md).

## Status

Projeto em construção. O fluxo de **login** está implementado; depois da autenticação o `app.py` ainda não renderiza nenhuma página (o bloco pós-login é `...`). Os pacotes `movies`, `reviews` e `actors` estão vazios, e `genres/page.py`/`genres/service.py` também. Existe apenas um `GenreRepository` parcial, ainda não ligado à interface.

## Features

- Tela de login Streamlit com usuário e senha
- `Auth.get_token()` chama `POST {BASE_URL}/auths/token/` e devolve `access`/`refresh`
- Token de acesso salvo em `st.session_state.token`; `st.rerun()` após o login
- Helper de logout que limpa o `session_state` (com bug, ver limitações)
- `GenreRepository` com `list_genres()` e `create_genre()` usando `Authorization: Bearer ...`
- `BASE_URL` carregada do `.env` via `python-dotenv`
- Lint com `flake8`/`isort`

## Stack

| Camada | Tecnologia / Versão |
|--------|---------------------|
| Linguagem | Python 3.14.8 |
| UI | Streamlit 1.66.1 |
| HTTP | requests 2.34.2 |
| Env | python-dotenv 1.2.4 |
| Backend | Flix API (Django REST + JWT) |
| Lint | flake8 7.4.1, isort 9.0.2 |

Dependências completas em [`requirements.txt`](requirements.txt); ferramentas de desenvolvimento em [`requirements_dev.txt`](requirements_dev.txt).

## Estrutura

```text
flix-app/
├── app.py                  # entrypoint Streamlit: login ou TODO pós-login
├── api/
│   ├── __init__.py         # carrega .env e expõe BASE_URL
│   └── service.py          # classe Auth (POST /auths/token/)
├── auth/
│   ├── page.py             # render_login()
│   └── service.py          # login() e logout()
├── genres/
│   ├── page.py             # vazio
│   ├── repository.py       # GenreRepository (list/create)
│   └── service.py          # vazio
├── movies/                 # apenas __init__.py
├── reviews/                # apenas __init__.py
├── actors/                 # apenas __init__.py
├── .env                    # BASE_URL (ignorado pelo git)
├── .flake8                 # exclui venv
├── requirements.txt
└── requirements_dev.txt
```

Não há `pyproject.toml`, testes automatizados nem `.env-example`.

## Integração com a Flix API

### Configuração

Crie `projetos/flix-app/.env` com a URL base da API, **sem barra no final**:

```dotenv
BASE_URL='http://127.0.0.1:8000/api/v1'
```

`api/__init__.py` chama `load_dotenv('.env')` e expõe `BASE_URL = os.getenv('BASE_URL')`. Por isso, execute o Streamlit a partir da pasta `flix-app`; caso contrário o `.env` não será encontrado.

### Endpoints usados

| Ação | Método e rota | Corpo/headers |
|------|---------------|---------------|
| Login | `POST {BASE_URL}/auths/token/` | form `username`, `password`; retorna `access` e `refresh` |
| Listar gêneros | `GET {BASE_URL}/genres/` | `Authorization: Bearer <access>` |
| Criar gênero | `POST {BASE_URL}/genres/` | `Authorization: Bearer <access>` + `name` |

O login só valida as credenciais. As rotas de CRUD da Flix API também exigem as permissões Django do usuário (`genres.view_genre`, `genres.add_genre`, etc.); superusuários passam em tudo. Detalhes em [`../flix-api/README.md`](../flix-api/README.md).

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
cat > .env <<'EOF'
BASE_URL='http://127.0.0.1:8000/api/v1'
EOF

# Rodar a interface
streamlit run app.py
```

Acesse `http://localhost:8501`, informe usuário e senha de um superusuário (ou de um usuário com as permissões necessárias) e faça login. Após o login, a página fica em branco porque as telas ainda não foram implementadas.

Para usar a API publicada, basta trocar o `BASE_URL` no `.env` (o ambiente local atual aponta para uma instância no PythonAnywhere).

## Limitações conhecidas

- `app.py`: após o login executa `...`; nenhuma tela de gêneros/filmes/avaliações é renderizada.
- `movies/`, `reviews/` e `actors/` contêm apenas `__init__.py`; `genres/page.py` e `genres/service.py` estão vazios.
- `GenreRepository.__headers` usa `f'Bearer {st.session_state}'` em vez de `st.session_state.token`; as chamadas de gêneros falhariam com 401.
- `logout()` chama `st.session_state.key()`, que não existe; o correto é `st.session_state.keys()`.
- `genres/repository.py` importa `response` de `urllib` sem usar e depois reutiliza o nome, gerando `F401`/`F811`; há também `E303` e `W391`.
- `Auth.get_token()` não trata timeout/erro de conexão e devolve `status_code` como `set`.
- Só o `access` é guardado; não há refresh automático nem expiração de sessão.
- O login não valida campos vazios e o `spinner` não é usado como context manager.
- Não há `.env-example`; o `.env` precisa ser criado manualmente.
- Sem testes automatizados.

Próximos passos sugeridos: corrigir os bugs de sessão/headers, implementar as páginas e services de gêneros, filmes, atores e avaliações, tratar refresh/expiração do JWT, adicionar `.env-example`, timeouts e testes.

## Licença

MIT — ver [../../LICENSE](../../LICENSE).
