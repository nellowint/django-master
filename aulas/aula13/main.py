# Aula 13

# POO - Programação Orientada a Objetos com Python

# Herança

"""
    Serve para herdar atributos e métodos de uma classe
        class ClasseFilha(ClassePai):
            pass
"""

class Carro:
    cor = 'Preto'
    portas = 5

    def acelerar(self):
        print('acelerando carro...')

    def ligar(self):
        print('ligando carro...')

    def desligar(self):
        print('desligar carro...')

    def trocar_marcha(self):
        print('trocando de marcha...')

carro = Carro()
carro.ligar()
carro.trocar_marcha()

class Fusca(Carro):
    modelo = 'Volkswagem'
    motor = 'Boxer'

fusca = Carro()
fusca.acelerar()

