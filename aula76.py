# video aula 119
# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])


# video aula 120
# Manipulando chaves e valores em dicionários

pessoa1 = {}
chave = 'nome' # criando uma chave dinámica

pessoa1[chave] = 'Luiz Otávio'
pessoa1['sobrenome'] = 'Miranda'

print(pessoa1[chave])

pessoa1[chave] = 'Maria'

print(pessoa1)

del pessoa1['sobrenome']
print(pessoa1)

# if pessoa1['sobrenome']: # isso não funciona porque o if quebra com a excessão KeyError
#     print('Não existe')

print(pessoa1.get('sobrenome')) # por padrão retorna None quando não existe. Posso colocar um vírgula depois da chave e um texto
if pessoa1.get('sobrenome') is None:
    print('Não Existe')
else:
    print(pessoa1['sobrenome'])

# video aula 121 e 122
'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
'''

print(len(pessoa))
print(len(pessoa1))

print(list(pessoa.keys()))
for chaves in pessoa.keys():
    print(chaves)

print(list(pessoa.values()))
for valor in pessoa.values():
    print(valor)

print(list(pessoa.items()))
for chave, valor in pessoa.items():
    print(chave, valor)

pessoa1.setdefault('idade', 0)
print(pessoa1['idade'])