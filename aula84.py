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