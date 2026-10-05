# Aula 14

# POO - Programação Orientada a Objetos com Python

# Polimorfismo

"""
    Subscreever os métodos de uma classe herdada
    auterando seus comportamentos
"""

class Animal:
    def emitir_som(self):
        print('Qualquer som...')


class Cachorro(Animal):

    def emitir_som(self):
        print('Au au...')

class Gato(Animal):

    def emitir_som(self):
        print('Miauuuu...')


cachorro = Cachorro()
cachorro.emitir_som()


gato = Gato()
gato.emitir_som()
