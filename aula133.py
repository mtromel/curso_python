'''
video aula 214
Encapsulamento (modificadores de acesso: public, protect, private)
Python NÃO TEM modificadores de acesso
Mas podemos seguir as seguintes convenções:
    (sem underline) = public
        pode ser usado em qualquer lugar
    _ (um underline) = protected
        não DEVE ser usado fora da classe ou suas subclasses
    __ (dois underline) = private
        "name mangling" (desfiguração de nome) em Python só DEVE ser usado na classe em que foi declarado.
"name mangling" = _NameClass__name_attr_or_method
'''

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é private'

    
    def metodo_publico(self):
        self._metodo_protected()
        print(self._protected)
        print(self.__private)
        self.__metodo_private()
        return 'metodo_publico'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'

f = Foo()
print(f.public)
print(f.metodo_publico())