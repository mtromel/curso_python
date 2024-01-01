'''
video aula 209
Métodos de classe + factories(fábricas)
São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, recebemos 
    a própria classe.
'''

class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # o metodo nomal de classe usa self
    def metodo_normal_de_classe(self):
        print('Hey')
    

    # o metodo de classe usa o decorator @classmethod e cls no lugar de self
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
    
    #factories method
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(Pessoa.ano)
Pessoa.metodo_normal_de_classe(p1) # nesse caso preciso passar o self
Pessoa.metodo_de_classe() # nesse caso não preciso passar nada porque o método vai usar a própria classe
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)

