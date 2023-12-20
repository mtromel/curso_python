# video aula 164
# variaveis livres + nonlocal

def fora(x):
    a = x

    def dentro():
        print(locals()) # mostra as variaveis locais desse escopo
        print()
        print(dentro.__code__.co_freevars) # mostra as variáveis livres desse escopo
        return a # aqui a variavel a é uma variável livre, porque não está definida na função dentro, e sim na função fora
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print('--------------------------')
print(dentro2())
print('--------------------------')

# def concatenar(string_inicial):
#     valor_final = string_inicial

#     def interna(valor_a_concatenar):
#         valor_final += valor_a_concatenar # dessa forma gera um erro porque a variavel valor_final é variável livre
#         return valor_final
#     return interna

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final # com esse comando o Python consegue concatenar a variavel livre
        print(f'Locals: ', locals())
        print(f'** {interna.__code__.co_freevars} **')
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)
