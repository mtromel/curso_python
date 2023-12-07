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

# video aula 122

import copy

d1 = {
    'c1' : 1,
    'c2' : 2,
    'l1' : [0, 1, 2],
}

# d2 = d1.copy() # dessa forma faz uma cópia rasa. Na copia rasa a alteração na lista l1 feita abaixo afeta os dois dicts
d2 = copy.deepcopy(d1) # aqui usa o módulo copy importado acima e faz uma cópia profunda.

d2['c1'] = 1000
d2['l1'][1] = 999999
print(d1)
print(d2)

# video aula 123

p1 = {
    'nome' : 'Luiz',
    'sobrenome' : 'Miranda'
}

# print(p1['nome'])
# print(p1.get('nome', 'Não exite'))

# nome = p1.pop('nome') # pop apaga a chave 'nome' do dicionário p1, mas salva o valor na variável nome.
# print(nome)
# print(p1)

# ultima_chave = p1.popitem() # popitem apaga a última chave do dicionário p1, mas salva como uma tupla na variável.
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'novo valor', # update atualiza o valor da chave nome e também insere uma nova chave valor.
#     'idade': 30,
# })

# p1.update(nome='novo valor', idade=30) # também pode ser usado o update passando argumentos nomeados e ele faz o mesmo que acima.

# outra forma de usar o update é passando uma lista ou tupla com os dados a serem atualizados
tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
# p1.update(tupla)
p1.update(lista)
print(p1)