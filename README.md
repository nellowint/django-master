# Django-Master — PycodeBR

Formação prática em desenvolvimento web com Python e Django, abrangendo fundamentos de programação, orientação a objetos, ambientes virtuais, desenvolvimento de sistemas web, banco de dados, ORM, templates, formulários, autenticação, Class-Based Views, Signals, PostgreSQL, APIs e deploy de aplicações na AWS. O curso também trabalha a construção de projetos práticos utilizando ferramentas e práticas aplicadas ao desenvolvimento de sistemas reais.

## O que você vai aprender

- Fundamentos Python: strings, operadores, condicionais, funções, loops, dicionários, listas, list comprehension
- Ambiente: `venv`, `pip`, `requirements.txt`, variáveis de ambiente (`os.environ`, `.env`)
- POO: classes e objetos, herança, polimorfismo (override e interface), `__init__`
- Django MVT: projetos vs apps, ORM, migrations, templates, formulários (`ModelForm`), autenticação, CBV e FBV
- Recursos Django: admin, static/media, signals (`pre_save`, `post_save`, `post_delete`), validações (`clean_*`)
- Banco de dados: SQLite em desenvolvimento, PostgreSQL pronto para produção
- Integração IA: cliente Google Gemini para geração de descrições (módulo `ia_api`)
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
│   └── carros/             # Projeto Django completo (ver README próprio)
│       ├── core/           # settings, urls, BaseModel, wsgi/asgi
│       ├── apps/cars/      # domínio Brand, Car, CarInventory
│       ├── apps/accounts/  # login, logout, register
│       ├── ia_api/         # cliente Gemini
│       ├── templates/      # base + cars + accounts
│       ├── static/         # css + img
│       ├── requirements.txt
│       └── .env-example
├── LICENSE
└── README.md
```

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

## Projeto prático

### Carros — CRUD Concessionária Django + IA

Monolito Django MVT com 2 apps (`cars`, `accounts`), CRUD de carros com upload de imagem, busca, autenticação, signals de inventário e limpeza de mídia, e cliente Gemini pronto para gerar descrições.

Documentação completa, setup e rotas em [`projetos/carros/README.md`](projetos/carros/README.md).

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

Para rodar o projeto Django, siga o quickstart do [`projetos/carros/README.md`](projetos/carros/README.md) (copiar `.env-example` para `.env`, `migrate`, `createsuperuser`, `runserver`).

## Créditos

Conteúdo didático do curso Django Master — PycodeBR. Implementação e anotações neste repositório por Wellinton Vieira.

## Licença

MIT — ver [LICENSE](LICENSE).
