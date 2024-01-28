'''
video aula 246
Classes decoradoras (Decorator classes)
'''


class Multiplicar:
    def __init__(self, func):
        self.func = func
        self.multiplicador = 10

    def __call__(self, *args, **kwds):
        resultado = self.func(*args, **kwds)
        return resultado * self.multiplicador


@Multiplicar
def soma(x, y):
    return x + y


dois_mais_dois = soma(2, 2)
print(dois_mais_dois)
