'''
video aula 201
Entendendo self em classes Python
self é uma convenção, poderia ser qualquer palavra, mas precisa ser o primeiro parametro de cada metodo
A Classe é o molde (geralmente sem dados)
A instância da classe é o objeto e tem vários dados
Uma classe pode gerar várias instâncias.
Na classe o self é a própria instância.
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