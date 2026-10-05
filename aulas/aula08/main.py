# Aula 08

# Dicionários em python

"""
    Dicionários são estruturas de dados que armazenam pares de chave-valor.
    Eles são utilizados para armazenar dados que possuem uma relação de chave-valor,
    onde a chave é única e o valor pode ser qualquer tipo de dado.
    Dicionários são mutáveis, ou seja, podemos adicionar, remover e alterar elementos.
    Dicionários são representados por chaves {} e os elementos são separados por vírgula.
    A chave e o valor são separados por dois pontos :.
"""

def imprime(dict):
    print(dict)

# exemplo de dicionário
pessoa = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}

imprime(pessoa)

# para acessar um item do dicionário podemos passar a chave
print(pessoa['nome'])

# método .get tambem acessa item do dicionário conforme a chave
print(pessoa.get('nome'))

# remover item do dicionario, é obrigatório passar a chave
pessoa.pop('cidade')

imprime(pessoa)

# para listar todas as chaves do dicionário
print(pessoa.keys())

# para listar apenas os items do dicionário
print(pessoa.values())

# para limpar tudo dentro do dicinário
pessoa.clear()

imprime(pessoa)

pessoa = {
    'nome': 'José',
    'idade': 20,
    'cidade': 'São Paulo',
    'skills': ['python', 'django', 'docker'],
    'pets': {
        'nome': 'trator',
        'idade': 10,
        'raça': 'vira lata'
    }
}

imprime(pessoa)

print(f'pets da pessoa: {pessoa.get('pets')['nome']}')

print(pessoa['pets']['raça'])


pessoa['ano_nasc'] = 1993

imprime(pessoa)

pessoa['pets']['cor'] = 'branco'

imprime(pessoa)

pessoa['endereco'] = {
        'rua': 'antonio nunes',
        'numero': 10,
        'cidade': 'São Paulo'
    }

imprime(pessoa)
