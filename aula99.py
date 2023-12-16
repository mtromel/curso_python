# video aula 158 e 159

import sys

# import aula99_package.modulo

# from aula99_package.modulo import soma_do_modulo, fala_oi
# from aula99_package import modulo
# from aula99_package.modulo import *
import aula99_package

print(__name__)
print(*sys.path, sep='\n')

print(aula99_package.soma_do_modulo(1,2))
print(aula99_package.variavel)
print(aula99_package.nova_variavel)
aula99_package.fala_oi()
