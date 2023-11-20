'''
Exercicio
Exiba os indices da lista
'''
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# tam = len(lista)
# i = 0
# for nome in lista:
#     print(i, nome, type(nome))
#     i += 1

# solução do professor:
indices = range(len(lista))

print(indices)

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))