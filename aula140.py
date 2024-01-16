'''
video aula 223, 224
Herança Múltipla - Python Orientado a Objetos
    Quer dizer que no Python, uma classe pode estender várias outras classes.
Herança Simples:
    Animal -> Mamifero -> Humano -> Pessoa -> Cliente
Herança múltipla e mixins (uma classe que não faz parte daquela familia)
    Log -> FileLog
    Animal -> Mamifero -> Humano -> Pessoa -> Cliente
    Cliente(Pessoa, Filelog)

A Herança múltipla pode gerar o problema do diamante:

A, B, C, D
D(B, C) - C(A) - B(A) - A

metodo -> falar (digamos que tenha esse método em A, em B e em C, e D chama ele. Qual o caminho que D vai fazer para escolher
    como executar esse método?)

            A
          /   \
          B    C
          \   /
            D
    
Python 3 usa C3 superclass linearization para gerar o mro.
Você não precisa estudar isso (é complexo)
https://en.wikipedia/org/wiki/C3_linearization

Para saber a ordem de chamada dos métodos use o método de classe Classe.mro()
    ou o atributo __mro__ (Dunder - Double Underscore)
'''

class A:
    ...

    def quem_sou(self):
        print('A')


class B(A):
    ...

    # def quem_sou(self):
    #     print('B')


class C(A):
    ...

    def quem_sou(self):
        print('C')

# essa é a herança múltipla
class D(B, C):
    ...

    # def quem_sou(self):
    #     print('D')


d = D()
d.quem_sou()
print(D.__mro__)
print(D.mro())