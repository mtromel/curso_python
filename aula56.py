"""
split e join com list e str
split - divide uma string (list)
join - une uma string
strip - corta os espaços do começo e do fim da string
rstrip - corta os espaços à direita da string
lstrip - corta os espaços à esquerda da string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)  # ao criar a string que vou usar o join preciso informar qual é o separador que vou utilizar. Nesse caso é  vírgula espaço
print(frases_unidas)
teste_frases = '-'.join('ABC')
print(teste_frases)