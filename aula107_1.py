'''
video aula 171 e 172
Considerando duas listas de inteiros ou floats (lista_a e lista_b)
Some os valores nas listas retornando uma nova lista com os valores somados.

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

================ resultado
lista_soma = [2, 4, 6, 8]
'''
def soma(lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    return [lista1[i] + lista2[i] for i in range(intervalo)]

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 1, 3, 4, 5]
lista_soma = []

lista_soma = soma(lista_a, lista_b)
print(lista_soma)


# solução do professor:
# solução que funciona em qualquer linguagem:

lista_soma1 = []

for i in range(len(lista_b)):
    lista_soma1.append(lista_a[i] + lista_b[i])

print(lista_soma1)

# solução com recursos do Python
lista_soma2 = []

for i, _ in enumerate(lista_b):
    lista_soma2.append(lista_a[i] + lista_b[i])

print(lista_soma2)

# solução mais elegante em Python
lista_soma3 = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma3)

# Como zip só une as listas até o tamanho da menor lista, uma outra possibilidade é usar o zip_longest
# para capturar os valores da lista maior

from itertools import zip_longest

lista_soma4 = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma4)