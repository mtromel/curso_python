'''
video aula 169
Exercício - unir listas
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas listas na ordem.
Use todos os valores da menor lista.
Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado:
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
'''

def unir_listas(lista1, lista2):
    resultado = []
    lista_menor = lista1 if len(lista1) < len(lista2) else lista2
    lista_maior = lista1 if len(lista1) > len(lista2) else lista2
    x = 0
    for item in lista_menor:
        resultado += [(item, lista_maior[x])]
        x += 1
    return resultado

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

lista_unida = unir_listas(cidades, estados)
print(lista_unida)

# solução do professor:
def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(intervalo)]

print(zipper(cidades,estados))

# o Python já tem essa função pronta:
print(list(zip(cidades, estados)))

# o Python tem um módulo que faz o contrário, ele pega a lista maior:
from itertools import zip_longest

print(list(zip_longest(cidades, estados))) # na execução padrão a função complementa a lista menor com None
print(list(zip_longest(cidades, estados, fillvalue='SEM CIDADE'))) # posso mudar o None para outro texto
