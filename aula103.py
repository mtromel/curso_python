'''
video aula 165
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções
'''
# essa é a função decoradora
# o trabalho dela é receber uma função, criar uma função interna para que eu tenha uma closure aqui dentro
# e essa função interna não será executada, ela será retornada sem execução, para que a pessoa que está usando
# essa função decoradora possa executar essa função e ai sim executar a função que está sendo decorada. Na decoração
# dessa função eu posso fazer alguma coisa, por exemplo, executar coisas antes ou depois do resultado da minha função
# ou seja, posso adicionar, remover, restringir ou até alterar o resultado da minha função interna se eu quiser
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)