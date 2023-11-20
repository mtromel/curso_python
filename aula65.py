'''
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parametros (argumentos) e retornar um valor específico.
Por padrão funções Python retornam none (nada).
'''

def imprimir(a, b, c):
    print(a, b, c)


imprimir(1, 2, 3)
imprimir('Marcos', 'Angela', 'Thiago')

def saudacao(nome='Sem nome'):
    print(f'Olá {nome}!')


saudacao('Marcos')
saudacao('Angela')
saudacao('Thiago')
saudacao()
