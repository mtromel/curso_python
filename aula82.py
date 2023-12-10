# video aula 134

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

'''
comparando lambda com def:
def     soma    (x, y)  :   return  x + y
lambda  ' '     x, y    :   ' '     x + y

no print abaixo o lambda tem mais um parametro: 2, 3. Esse argumento é para atender ao parametro *args da função executa
'''

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# é possivel usar lambda no lugar de cria_multiplicador, mas deixa o código confuso então melhor não usar. Seria assim:
duplica = executa(lambda m: lambda n: n* m, 2)
print(duplica(2))

# exemplo de uso de lambda
print(executa(lambda x, y: x + y, 2, 3))
print(executa(soma, 2, 3))
print(soma(2, 3))

# também posso usar *args
print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7))