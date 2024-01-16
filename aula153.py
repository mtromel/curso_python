'''
video aula 245
Método especial __call__
callable é algo que pode ser executado com parênteses
Em classes normais, __call__ faz a instância de uma classe "callable"
'''

from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 2134

call1 = CallMe('23945876545')
retorno = call1('Luiz Otávio') # sem o método __call_ na classe esse comando retorna erro 
print(retorno)