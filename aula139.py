'''
video aula 221, 222
super () é a super classe na sub classe

Classe principal (Pessoa)
    -> supler class, base class, parent class
Classes filhas (Cliente)
    -> sub class, child class, derived class
'''

class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs)

    def metodo(self):
        super().metodo() # B
        super(B, self).metodo # A
        A.metodo(self) # posso chamar assim, mas o recomendado é usar o super()
        B.metodo(self)
        print('C')

print(C.mro())
print(B.mro())
print(A.mro())

c = C('Atributo', 'Qualquer')
print(c.atributo)
print(c.outra_coisa)
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()