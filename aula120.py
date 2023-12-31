'''
video aula 198, 199
class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que podem ter seus próprios atributos (dados dentro da classe) 
    e métodos (ações dentro da classe).
Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.
Por convenção, usamos PascalCase para nomes de classes.
def dentro da classe não cria uma função, cria um método.
o método __init__ é um dos primeiros a ser chamado para inicializar os atributos da classe.
o self referencia à instância da classe
'''

# string = 'Luiz' # é uma instância de str
# print(string.upper())

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Luiz', 'Otávio')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)

