'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''

# Definição
def soma(x, y):
    print(f'{x=} y={y}', '|', 'x + y = ', x + y)

# chamada da função com argumento não nomeado ou posicional
soma(1, 2)

# chamada da função com argumento nomeado
# é posssível usar argumentos posicionais junto com nomeados, mas a partir do nomeado todos os depois dele também precisam ser nomeados.
soma(y=2, x=1)

