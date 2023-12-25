'''
video aula 178
reduce - faz a redução de um iterável em um valor
'''
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

total = 0
for p in produtos:
    total += p['preco']

print(total)

# com sum() o resultado é o mesmo
print(sum([p['preco'] for p in produtos]))

# com reduce()
def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco'] 

total1 = reduce(funcao_do_reduce, produtos, 0) # o zero aqui é o valor inicial.

print('total1', total1)

# usando lambda ficaria assim:

total2 = reduce(lambda acumulador, produto: acumulador + produto['preco'], produtos, 0)

print ('total2', total2)