'''
video aula 218
Exercício com classes
1 - Crie uma classe Carro (nome)
2 - Crie uma classe Motor (nome)
3 - Crie uma classe Fabricante (nome)
4 - Faça a ligação entre Carro tem um Motor
    Obs.: Um motor pode ser de vários carros
5 - Faça a ligação entre Carro e um Fabricante
    Obs.: Um fabricante pode fabricar vários carros
Exiba o nome do carro, motor e fabricantes na tela
'''

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
    
    def imprimir_carro(self):
        print(self.fabricante.nome, self.nome, self.motor.nome)

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

gol = Carro('Gol')
idea = Carro('Idea')
tcros = Carro('T Cross')
hilux = Carro('Hilux')
saveiro = Carro('Saveiro')
gasolina16 = Motor('Gasolina 1.6')
flex14 = Motor('Flex 1.4')
flex20 = Motor('Flex 2.0')
diesel = Motor('Diesel 3.0')
volkswagen = Fabricante("Volkswagen")
fiat = Fabricante('Fiat')
toyota = Fabricante('Toyota')

gol.motor = gasolina16
gol.fabricante = volkswagen
saveiro.motor = gasolina16
saveiro.fabricante = volkswagen
idea.motor = flex14
idea.fabricante = fiat
tcros.motor = flex20
tcros.fabricante = volkswagen
hilux.motor = diesel
hilux.fabricante = toyota

Carro.imprimir_carro(gol)
Carro.imprimir_carro(idea)
Carro.imprimir_carro(tcros)
Carro.imprimir_carro(hilux)
Carro.imprimir_carro(saveiro)
