'''
video aula 133
Função lambda em Python
A função lambda é uma função como qualquer outra em Python. Porém são funções anônimas que contém apenas uma linha.
    Ou seja, tudo deve ser contido dentro de uma única expressão.
'''

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

lista1 = [4, 32, 1, 34, 5, 6, 21,]
lista1.sort() # essa função faz a ordenação diretamente dentro da lista original
sorted(lista1) # essa função faz a mesma coisa de sort, mas faz uma copia rasa da lista original e ordena a cópia.
print(lista1)

lista1.sort(reverse=True) 
print(lista1)

# lista.sort() # se passar assim apenas vai dar erro porque a lista tem dicionários dentro.
# print(lista)

# para evitar o erro preciso de uma função
# def ordena(item):
#     return item['sobrenome']

# lista.sort(key=ordena)

# usando lambda não preciso criar a função ordena
def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)

#também posso usar a forma que altera a lista original.
lista.sort(key=lambda item: item['nome'])

for item in lista:
    print(item)
