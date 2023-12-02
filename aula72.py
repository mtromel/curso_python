'''
aula 113
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável.

Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
'''

print(1*2*3*4*5)

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def par_impar(x):
    resultado = x % 2
    if resultado == 0:
        return True
    return False

retorno = multiplica(5, 5)
print('O total da multiplicação é', retorno)

verifica_par_impar = par_impar(retorno)
if verifica_par_impar:
    print(f'O número {retorno} é par')
else:
    print(f'O número {retorno} é impar')

