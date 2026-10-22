# Django-Master — PycodeBR

Formação prática em desenvolvimento web com Python e Django, abrangendo fundamentos de programação, orientação a objetos, ambientes virtuais, desenvolvimento de sistemas web, banco de dados, ORM, templates, formulários, autenticação, Class-Based Views, Signals, PostgreSQL, APIs REST com Django REST Framework (DRF) e JWT, e deploy de aplicações na AWS. O curso também trabalha a construção de projetos práticos utilizando ferramentas e práticas aplicadas ao desenvolvimento de sistemas reais.

## O que você vai aprender

- Fundamentos Python: strings, operadores, condicionais, funções, loops, dicionários, listas, list comprehension
- Ambiente: `venv`, `pip`, `requirements.txt`, variáveis de ambiente (`os.environ`, `.env`)
- POO: classes e objetos, herança, polimorfismo (override e interface), `__init__`
- Django MVT: projetos vs apps, ORM, migrations, templates, formulários (`ModelForm`), autenticação, CBV e FBV
- Recursos Django: admin, static/media, signals (`pre_save`, `post_save`, `post_delete`), validações (`clean_*`)
- Django REST: serializers, views genéricas (`ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`), `APIView`, permissões e autenticação JWT (`SimpleJWT`)
- Documentação de API: OpenAPI/Swagger/Redoc com `drf-spectacular`; países com `django-countries`
- Banco de dados: SQLite em desenvolvimento, PostgreSQL pronto para produção no projeto `carros`
- Boas práticas: organização por apps, `BaseModel` abstrato com auditoria, `.env-example`, i18n `pt-br`

## Estrutura do repositório

```text
django-master/
├── aulas/                  # 15 aulas de base Python + POO
│   ├── aula01/main.py      # Hello World
│   ├── aula02/main.md      # venv
│   ├── aula03/main.md      # pip
│   ├── aula04/main.py      # strings
│   ├── aula05/main.py      # operadores e condicionais
│   ├── aula06/main.py      # funções e lambda
│   ├── aula07/main.py      # for / while
│   ├── aula08/main.py      # dicionários
│   ├── aula09/main.py      # listas
│   ├── aula10/main.py      # list comprehension
│   ├── aula11/main.py      # variáveis de ambiente
│   ├── aula12/main.py      # POO básico
│   ├── aula13/main.py      # herança
│   ├── aula14/main.py      # polimorfismo (override)
│   └── aula15/main.py      # interface + __init__
├── projetos/
│   ├── carros/             # Projeto Django MVT (ver README próprio)
│   │   ├── core/           # settings, urls, BaseModel, wsgi/asgi
│   │   ├── apps/cars/      # domínio Brand, Car, CarInventory
│   │   ├── apps/accounts/  # login, logout, register
│   │   ├── templates/      # base + cars + accounts
│   │   ├── static/         # css + img
│   │   ├── uwsgi.ini       # deploy
│   │   ├── requirements.txt
│   │   └── .env-example
│   └── flix-api/           # Projeto Django REST (ver README próprio)
│       ├── core/           # settings, urls, BaseModel, permissions
│       ├── apps/actors/    # CRUD + importação CSV de atores
│       ├── apps/genres/    # CRUD de gêneros
│       ├── apps/movies/    # CRUD + estatísticas
│       ├── apps/reviews/   # CRUD de avaliações
│       ├── apps/auths/     # endpoints JWT (token/refresh/verify)
│       ├── static/actors.csv
│       ├── requirements.txt
│       └── .env-example
├── LICENSE
└── README.md
```

Os dois projetos Django são independentes: cada um tem seu próprio `venv`, `requirements.txt`, `.env-example` e banco SQLite local. Não há tooling nem código compartilhado na raiz.

## Grade das aulas

| Aula | Arquivo | Tópico | Conceitos-chave |
|------|---------|--------|-----------------|
| 01 | `aulas/aula01/main.py` | Introdução | `print()` |
| 02 | `aulas/aula02/main.md` | Ambiente virtual | `python -m venv venv`, `source venv/bin/activate`, `deactivate` |
| 03 | `aulas/aula03/main.md` | pip | `pip install`, `pip freeze > requirements.txt`, `pip install -r requirements.txt` |
| 04 | `aulas/aula04/main.py` | Strings | index/slice, `len`, `count`, `find`, `upper`, `lower`, `split`, `join`, `strip` |
| 05 | `aulas/aula05/main.py` | Lógica e comparação | `and`, `or`, `not`, `in`, `==`, `!=`, `if/else` |
| 06 | `aulas/aula06/main.py` | Funções | `def`, `return`, `print/len/type`, `lambda` |
| 07 | `aulas/aula07/main.py` | Loops | `for`, `while`, `enumerate`, `range`, `break`, `continue` |
| 08 | `aulas/aula08/main.py` | Dicionários | `[]`, `.get()`, `pop`, `keys`, `values`, aninhados |
| 09 | `aulas/aula09/main.py` | Listas | `append`, `insert`, `pop`, `del`, `remove`, `reverse`, `sort` |
| 10 | `aulas/aula10/main.py` | List comprehension | `[expr for item in items]`, filtro `if`, uso com funções |
| 11 | `aulas/aula11/main.py` | Variáveis de ambiente | `os.environ.get()` |
| 12 | `aulas/aula12/main.py` | POO básico | classe, instância, `self`, atributos e métodos |
| 13 | `aulas/aula13/main.py` | Herança | `class Filha(Pai)`, reuso de atributos/métodos |
| 14 | `aulas/aula14/main.py` | Polimorfismo | override de `emitir_som()` em `Cachorro`/`Gato` |
| 15 | `aulas/aula15/main.py` | Interface + construtor | `Forma.area()`, `Quadrado`/`Circulo` com `__init__` |

Progressão: setup (01-03) → base (04-05) → controle (06-07) → coleções (08-10) → config (11) → POO (12-15).

## Projetos práticos

### Carros — CRUD de concessionária (Django MVT)

Monolito Django MVT com 2 apps (`cars`, `accounts`), CRUD de carros com upload de imagem, busca, autenticação, signals de inventário e limpeza de mídia. Não há módulo de IA no código: `GEMINI_API_KEY` ainda é lida em `settings.py` e resta apenas um comentário de gancho em `signals.py`.

Documentação completa, setup e rotas em [`projetos/carros/README.md`](projetos/carros/README.md).

### Flix API — catálogo de filmes (Django REST)

API REST com DRF, autenticação JWT (`SimpleJWT`), permissões por modelo, serializers aninhados para leitura, endpoint de estatísticas, documentação OpenAPI/Swagger (`drf-spectacular`) e importação de atores via CSV. Todos os recursos ficam sob `/api/v1/`.

Documentação completa, rotas e payloads em [`projetos/flix-api/README.md`](projetos/flix-api/README.md).

## Como estudar e executar

Pré-requisitos: Python 3.14, `pip`, `venv`.

```bash
# 1. Clonar
git clone <url-do-repo> django-master
cd django-master

# 2. Executar uma aula qualquer (não precisa de dependências)
python aulas/aula04/main.py
python aulas/aula06/main.py
python aulas/aula12/main.py

# 3. Praticar ambiente isolado (conforme aulas 02 e 03)
python -m venv venv
source venv/bin/activate
pip install -r projetos/carros/requirements.txt
pip freeze > requirements.txt
deactivate
```

Para rodar um projeto Django, use o quickstart do README correspondente:

- Carros: `cd projetos/carros`, copiar `.env-example` para `.env`, instalar `requirements.txt`, rodar `migrate`, `createsuperuser` e `runserver`.
- Flix API: `cd projetos/flix-api`, copiar `.env-example` para `.env`, instalar `requirements.txt`, rodar `migrate`, `createsuperuser` e `runserver`.

> **Atenção (flix-api):** `core/settings.py:118` usa `STATIC_ROOT = BASE_DIR + '/staticfiles'`; como `BASE_DIR` é `pathlib.Path`, isso levanta `TypeError` e qualquer comando `manage.py` falha. Troque por `BASE_DIR / 'staticfiles'` antes de rodar. O README do projeto detalha a limitação.

Cada projeto já possui um `venv/` local no repositório de estudo; se recriar o ambiente, use os comandos das aulas 02 e 03.

## Créditos

Conteúdo didático do curso Django Master — PycodeBR. Implementação e anotações neste repositório por Wellinton Vieira.

## Licença

MIT — ver [LICENSE](LICENSE).
