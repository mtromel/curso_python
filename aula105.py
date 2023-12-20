'''
video aula 167
Decoradores com parâmetros
'''
# as funções decoradoras são factory functions
def fabrica_de_decoradores(a=None, b=None, c=None): # esse é um recurso da linguagem que utiliza o escopo da função para passar parâmetros para a função decoradora
    def fabrica_de_funcoes(func): # esse é o decorador, deve sempre receber uma função
        print('Decoradora 1')

        def aninhada(*args, **kwargs): # a função aninhada pode receber o que quisermos
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y 

multiplica = fabrica_de_decoradores(1, 2, 3)(lambda x, y: x * y) # isso é a mesma coisa que as linhas abaixo:
# decoradora = fabrica_de_decoradores()
# multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)