'''
video aula 205
__dict__ e vars para atributos de instâncias
'''
class Pessoa:
    ano_atual = 2023 # esse é um atributo da classe, ele é usado por todas as instâncias

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('João', 35)
print(p1.__dict__)
print(vars(p1))