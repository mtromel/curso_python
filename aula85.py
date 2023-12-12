'''
video aula 139
For dentro de for em list comprehension
'''

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

lista1 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista)
print()
print(lista1)