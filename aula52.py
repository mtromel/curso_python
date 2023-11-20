'''
Tipo tupla - uma lista imutável
'''
# isso é uma tupla:
nomes = 'Maria', 'Helena', 'Luiz'
# outra forma de criar uma tupla:
nomes1 = ('Angela', 'Marcos', 'Thiago')

# é possivel também converter lista em tupla
nomes2 = ['Thiago', 'Angela', 'Marcos']
nomes3 = tuple(nomes2)

# também é possivel mudar uma tupla em uma lista
nomes4 = list(nomes)


print(nomes[0])
print(nomes, type(nomes))
print(nomes1, type(nomes1))
print(nomes2, type(nomes2))
print(nomes3, type(nomes3))
print(nomes4, type(nomes4))



