'''
video aula 236, 237, 238
Python Special Methods, Magic Methods ou Dunder Methods
Dunder = Double Underscore = __dunder__
Antigo e útil: https://rszalski.github.io/magicmethods/
https://docs.python.org/3/reference/datamodel.html#specialnames

__lt__(self, other) - self < other
__le__(self, other) - self <= other
__gt__(self, other) - self > other
__ge__(self, other) - self >= other
__eq__(self, other) - self == other
__ne__(self, other) - self != other
__add__(self, other) - self + other
__sub__(self, other) - self - other
__mul__(self, other) - self * other
__truediv__(self, other) - self / other
__neg__(self) - -self
__str__(self) - str
__repr__(self) - str
'''

class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z
    
    # se tiver o método __str__ vai chamar esse método primeiro, se não tiver vai chamar o __repr__
    # def __str__(self):
    #     return f'({self.x}, {self.y})'

    # o método __repr__ normalmente uso para comunicar com desenvolvedores, tipo dizer como quero que implemente essa classe
    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__ # faz o mesmo que na linha acima
        return f'{class_name}(x={self.x!r}, y={self.y!r})' # o !r faz o python mostrar a representação do objeto
                                                                         # no caso da string vai mostrar entre aspas, para não
                                                                         # ter dúvida se estou esperando uma string ou um obj
                                                                         # isso precisa ser feito sempre que usar o __repr__
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other
    
p1 = Ponto(1, 2)
p2 = Ponto(978, 876)
p3 = p1 + p2
print(p3)
print('P1 é maior que P2', p1 > p2)
print('P2 é maior que P1', p2 > p1)

# print(p1) # retorno a o método __str__
# print(repr(p2)) # retorna o método __repr__
# print(f'{p2}') # retorna o método __str__
# print(f'{p2!s}') # retorna o método __str__
# print(f'{p2!r}') # retorna o método __repr__

