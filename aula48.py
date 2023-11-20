'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas

Create, Read, Update, Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

#  string = 'ABCDE'  # 5 caracteres
#  lista = list()
#  lista = []  # cria uma lista vazia
#  lista = [123, True, 'Marcos Cristiano', 1.2, []]
#  lista[2] = 'Maria'
#  print(bool(lista[2]), type(lista[2]))  # falsy  quando a lista está vazia
#  print(lista[-3].upper(), type(lista))
#  print(lista[-3], type(lista[2]))

# lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
# lista.append('BBB')  # aiciona no final da lista
# print(lista)
# ultimo_valor = lista.pop()  #  remove o último item da lista
# lista.pop(3)  # permite remover do meio da lista, só precisa tomar cuidado quando a lista for muito grande, isso pode exigir muito processamento
# lista.append(60)
# lista.append(70)
# lista.insert(0, 5)
# print(lista, 'Removido', ultimo_valor)
# print(lista, 'Removido', lista.pop())

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_d = lista_a.extend(lista_b)
# print(lista_d)

'''
Cuidados com dados mutáveis
= - copiado o valor(imutáveis)
= - aponta para o mesmo valor na memória (mutável)
'''

lista_a = ['Marcos', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
