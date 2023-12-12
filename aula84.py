'''
video aula 136
List comprehension em Python
List comprehension é uma forma rápida para criar listas a partir de iteráveis.
'''

# para mostrar na tela uma lista com 10 números posso fazer assim:
print(list(range(10)))

# se eu quiser criar uma lista similar posso fazer assim:
lista = []
for numero in range(10):
    lista.append(numero)
print('Lista do FOR: ', lista)

# usando list comprehension é assim:
lista1 = [numero for numero in range(10)]
print('Lista do list comprehension: ', lista1)

# posso fazer operações lógicas também:
lista2 = [
    numero * 2 
    for numero in range(10)
]
print('Lista do list comprehension com lógica: ', lista2)

'''
video aula 137
Mapeamento de dados em list comprehension
'''

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [
    {'nome': produto['nome'], 'preco': produto['preco']}
    for produto in produtos
]

print(novos_produtos)
print(*novos_produtos, sep='\n')

novos_produtos1 = [
    {**produto}
    for produto in produtos
]

print(novos_produtos1)
print(*novos_produtos1, sep='\n')

novos_produtos2 = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]

print(novos_produtos2)
print(*novos_produtos2, sep='\n')

novos_produtos3 = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(novos_produtos3)
print(*novos_produtos3, sep='\n')

'''
video aula 138
Filtro em list comprehension
'''

novos_produtos4 = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]

print(novos_produtos4)
print(*novos_produtos4, sep='\n')