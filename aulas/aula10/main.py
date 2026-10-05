# Aula 10

# Compreensão de Listas

"""
    Compreensão de Listas é um recurso em python onde podemos aplicar uma função/expressão para cada um dos items da lista, ou seja,
    retorna uma nova lista conforme a expressão/função aplicada dentro da lista
    sintaxe [ expressão for item in items ]
"""

# exemplo sem compreensão de listas

numeros = [2, 3, 5, 6, 8]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros)
print(numeros_dobrados)


# exemplo usando compreensão de listas
numeros = [2, 3, 5, 6, 8]
numeros_dobrados = [ numero * 2 for numero in numeros]

print(numeros)
print(numeros_dobrados)

# exemplo usando uma função

def dobrar_numero(numero):
    return numero * 2

numeros = [2, 3, 5, 6, 8]
numeros_dobrados = [ dobrar_numero(numero) for numero in numeros]

print(numeros)
print(numeros_dobrados)

# exemplo com strings

frutas = ['maça', 'banana', 'caju', 'melancia', 'abacate', 'melão', 'uva', 'pera']

frutas_maiusculas = [ fruta.upper() for fruta in frutas ]

print(frutas)
print(frutas_maiusculas)

# exemplo com strings, elementos em maíusculas somente com a incial 'M'

frutas = ['maça', 'banana', 'caju', 'melancia', 'abacate', 'melão', 'uva', 'pera']

frutas_maiusculas = [ fruta.upper() for fruta in frutas if fruta[0] == 'm' ]

print(frutas)
print(frutas_maiusculas)
