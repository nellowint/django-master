#Aula 09

# Listas em python

"""
    Listas são estruturas de dados em python para organizar elementos
    Listas podem receber qualquer tipo de dados em python
"""
def imprime(list):
    print(list)

frutas = ['maça', 'banana', 'abacate', 'melancia', 'uva', 'laranja', 'pera']

imprime(frutas)

# append para inserir elemento na lista, append sempre insere ao final da lista

frutas.append('caju')

imprime(frutas)

# insert para inserir elemento conforme o índice passado em parametro

frutas.insert(1, 'melão')
imprime(frutas)

"""
    Para remover elemento de uma lista há três maneiras
    pop - remove o ultimo elemento
    del list[indice] - remove conforme o indice passado em parametro
    list.remove('element') - remove conforme o elemento passado em parametro
"""

frutas.pop()
imprime(frutas)

del frutas[3]
imprime(frutas)

frutas.remove('maça')
imprime(frutas)

"""
    Funções para ordenação em listas
    sort - ordenar por ordem precedência numérica ou alfabética
    reverse - inverter lista conforme a ordem numérica ou alfabética
"""

frutas.reverse()
imprime(frutas)

frutas.sort()
imprime(frutas)
