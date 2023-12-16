
# com esse método __all__ criado só será importado para o outro módulo o que estiver informado dentro dessa lista
__all__ = [
    'soma_do_modulo',
    'variavel',
    'nova_variavel',
]

from aula99_package.modulo_b import fala_oi

def soma_do_modulo(x, y):
    return x + y

variavel = 'Alguma coisa'

nova_variavel = 'OK'

# fala_oi()