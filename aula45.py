'''
Iterável -> str, range, etc ( tem um método dentro dele, é o metodo __iter__ ) '__' = dunder
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)

texto = iter('Marcos')  # __iter__()

print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(texto.__next__())

# for letra in texto:
#     print(letra)

texto1 = 'Tromel'
iteratador = iter(texto)  # iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break



