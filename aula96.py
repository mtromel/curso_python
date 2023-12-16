'''
video aula 153
Módulos padrão do Python (import, from, as e *)
https://docs.python.org/3/py-modindex.html
inteiro - import nome_modulo
Vantagens: você tem o namespace do módulo
Desvantagens: nomes grandes
'''
# import sys

# print(sys.platform)

'''
partes - from nome_modulo import objeto1, objeto2
Vantagens: nomes pequenos
Desvantagens: Sem o namespace do módulo
'''
# from sys import exit, platform, stdin

# print(platform)

'''
alias 1 - import nome_modulo as apelido
alias 2 - from nome_modulo import objeto as apelido
Vantagens: você pode reservar nomes para seu código
Desvantagens: pode ficar for do padrão da linguagem
'''
# import sys as s

# sys = 'alguma coisa' # nesse caso é melhor mudar o nome da variável
# print(s.platform)
# print(sys)

# from sys import platform as pf, exit as ex 
# print(pf)

'''
má prática - from nome_modulo import *
Vantagens: importa tudo de um módulo
Desvantagens: importa tudo de um módulo
'''

# from sys import *
# print(platform)
# exit()