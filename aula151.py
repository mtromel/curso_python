'''
video aula 243
Funções decoradoras e decoradores com classes
'''
# é possível fazer dessa forma tambémm, só remover as heranças das classes e adicionar o decorador @adiciona_repr.
# se não usasse o decorador precisar adicionar o código abaixo depois da criação das classes:
# Time = adiciona_repr(Time)
# Planeta = adiciona_repr(Planeta)

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls

# class MyReprMixin:
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr

# class SuperTime:
#     ...

@adiciona_repr
class Time():
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Planeta():
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)