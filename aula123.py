'''
video aula 202
Escopo da classe e de métodos da classe

'''

class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comento {alimento}'
    
    def executar(self, *args, **kwargs):
        return self. comendo(*args, **kwargs)

leao = Animal('Leão')
print(leao.nome)
print(leao.comendo('maçã'))
print(leao.executar('maçã'))