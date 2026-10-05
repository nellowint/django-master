# Aula 04

#String é um tipo primitido de dados
#String nada mais é que uma cadeia de caracteres, ou seja, um conjunto de letras, números e símbolos.

#Exemplos de string
texto="Eu sou um texto de exemplo"
print(texto)

print(texto[5]) #imprime a letra "s" que está na posição 5 da string

#Para capturar trechos de uma string, podemos utilizar o fatiamento de strings, que é feito utilizando colchetes e dois pontos.
print(texto[0:6]) #imprime "Eu" que está na posição 0 e 1 da string

print(texto[3:10]) #imprime "sou uma" que está na posição 3 até a posição 10 da string

print(texto[10:17]) #imprime "exemplo" que está na posição 10 até a posição 17 da string

print(len(texto)) #imprime o tamanho da string, que é 17

print(texto.count("s")) #imprime a quantidade de vezes que a letra "s" aparece na string, que é 2

print(texto.find("exemplo")) #imprime a posição da palavra "exemplo " na string, que é 10

print(texto.upper()) #imprime a string em letras maiúsculas

print(texto.lower()) #imprime a string em letras minúsculas

print(texto.capitalize()) #imprime a string com a primeira letra maiúscula e o restante minúsculo

print(texto.title()) #imprime a string com a primeira letra de cada palavra maiúscula

print(texto.split()) #divide a string em uma lista de palavras, utilizando o espaço como separador

lista_palavras=texto.split() #divide a string em uma lista de palavras, utilizando o espaço como separador
print(''.join(lista_palavras)) #junta a lista de palavras em uma única string, sem espaços
print(' '.join(lista_palavras)) #junta a lista de palavras em uma única string, com espaços
print('-'.join(lista_palavras)) #junta a lista de palavras em uma única string, com hífens


texto2="    Eu sou um texto de exemplo   "
print(texto2.strip()) #remove os espaços em branco do início e do final da string

print(texto2.lstrip()) #remove os espaços em branco do início da string

print(texto2.rstrip()) #remove os espaços em branco do final da string



