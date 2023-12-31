'''
video aula 204
Atributos de classe
'''

class Pessoa:
    ano_atual = 2023 # esse é um atributo da classe, ele é usado por todas as instâncias

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100 # muda o atributo na instância
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade # aqui posso usar o self.ano_atual mas corro o risco de ter o valor alterado
                                                # na instancia. Primeiro ele procura na instancia, depois na classe.
    

p1 = Pessoa('João', 35)
p2 =Pessoa('Helena', 12)
print(Pessoa.ano_atual) # posso usar o atributo da classe aqui fora também.
# Pessoa.ano_atual = 1  muda o atributo da classe para todas as instâncias
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())