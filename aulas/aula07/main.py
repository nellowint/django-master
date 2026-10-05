# Aula 07 

## Laços de repetição
"""
    Para percorrer uma lista de elementos, podemos utilizar o laço de repetição for.

    while é utilizado quando não sabemos o número de iterações que serão realizadas, 
    enquanto for é utilizado quando sabemos o número de iterações que serão realizadas.

"""

frutas = ['maçã', 'banana', 'laranja', 'uva']


# laço de repetição com for
for fruta in frutas:
    print(fruta)

# enumerate é utilizado para obter o índice do elemento da lista
for indice, fruta in enumerate(frutas):
    print(f"indice: {indice} | item: {fruta}")

# range é utilizado para gerar uma sequência de números
for i in range(5):
    print(i)

# while é utilizado quando não sabemos o número de iterações que serão realizadas

i = 0
while i < 10:
    print(f"i: {i} | i ainda é menor que 10")
    i += 1

"""
    Qunando utilizar for ou while?
    - for é utilizado quando sabemos o número de iterações que serão realizadas.
    - while é utilizado quando não sabemos o número de iterações que serão realizadas.
"""


# função break é utilizada para interromper o laço de repetição
for fruta in frutas:
    if fruta == 'banana':
        print(f"encontrei a fruta {fruta}")
        break
    print(f"não encontrei a fruta {fruta}")


# continue é utilizado para pular a iteração atual e continuar para a próxima
for indice, fruta in enumerate(frutas):
    if indice == 2:
        continue
    print(f"fruta: {fruta}")

