'''
video aula 141
Dictionary Comprehension e Set Comprehension
'''

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# dictionary comprehension

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave == 'categoria'
}

print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    chave: valor 
    for chave, valor in  lista
}

dc1 = dict(dc)

print(dc)
print(dc1)

# set comprehension

