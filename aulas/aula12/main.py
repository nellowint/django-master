# Aula 12

# POO - Programação Orientada a Objetos com Python

"""
    O que é ?
        "Abstração de um objeto do mundo real para a computação"

        em python usamos classes para definir objetos

        self - é uma instancia da própria classe
"""

class Monitor:
    marca='AOC'
    tamanho=27
    frequencia=144

    def ligar(self):
        print('Ligando monitor')

    def desligar(self):
        print('Desligando monitor')

    def diminuir_resolucao(self, valor):
        return self.frequencia - valor

monitor = Monitor()

print(monitor.marca)

monitor.ligar()

nova_resolucao = monitor.diminuir_resolucao(60)

print(nova_resolucao)


