'''
video aula 135
Empacotamento e desempacotamento de dicionários
'''
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

a, b = pessoa
print(a, b)

a, b = pessoa.values()
print(a, b)

a, b = pessoa.items()
print(a, b)

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)

pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa)

# args e kwargs
# args (já vimos) - argumentos não nomeados
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)

    for chave, valor in  kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, nome='Joana', qld=123)
mostro_argumentos_nomeados(**pessoas_completa)