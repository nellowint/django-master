# Aula 06

# Funções em python

"""
    Funções são blocos de código que podem ser reutilizados em diferentes partes do programa. 
    Elas permitem organizar o código, tornando-o mais legível e modular. 
    Em Python, funções são definidas usando a palavra-chave `def`, seguida pelo nome da função e parênteses que podem conter parâmetros
"""

def saudacao():
    print("Olá! Bem-vindo(a) à aula de funções em Python.")

saudacao()  # Chamando a função saudacao

"""
    Funções nativas em Python são funções que já vêm incorporadas na linguagem e podem ser usadas diretamente sem a necessidade de defini-las.
    Alguns exemplos de funções nativas incluem:
    - print(): Exibe informações na tela.
    - len(): Retorna o tamanho de uma sequência (como listas, strings, etc.).
    - type(): Retorna o tipo de dado de um objeto.
"""

# Função input() é usada para receber dados do usuário. 
# Ela pausa a execução do programa e espera que o usuário digite algo, retornando o valor digitado como uma string.
# nome = input("Digite seu nome: ")
# print(f"Olá, {nome}! Seja bem-vindo(a) à aula de funções em Python.")

def somar(parametro1, parametro2):
    """
    Esta função recebe dois parâmetros e retorna a soma deles.
    """
    resultado = parametro1 + parametro2
    return resultado

minha_soma = somar(5, 10)  # Chamando a função somar com os argumentos 5 e 10
print(f"O resultado da soma é: {minha_soma}")

"""
    Funções lambda são funções anônimas, ou seja, funções sem nome, que podem ser definidas em uma única linha.
    Elas são úteis para operações simples e podem ser usadas como argumentos para outras funções.
    A sintaxe básica de uma função lambda é:
    lambda argumentos: expressão
"""

lambda_somar = lambda x, y: x + y  # Definindo uma função lambda que soma dois números
resultado_lambda = lambda_somar(3, 7)  # Chamando a função lambda
print(f"O resultado da soma usando lambda é: {resultado_lambda}")