# Aula 15

# POO - Programação Orientada a Objetos com Python

# Polimorfismo de Interface

class Forma:

    def area(self):
        pass

class Quadrado(Forma):

    # __init__ é o método construtor da classe
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2



quadrado = Quadrado(10)
print(f'Area: {quadrado.area()}')

class Circulo(Forma):

    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2

circulo = Circulo(2)
print(f'Area: {int(circulo.area())}')
