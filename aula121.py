'''
video aula 200
Métodos em instâncias de classes Python
Hard coded - é algo que foi escrito diretamente no código
'''

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
celta = Carro('Celta')

print(fusca.nome)
fusca.acelerar()
print(celta.nome)
celta.acelerar()