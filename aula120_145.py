'''
video aula 196
Controlando a quantidade de argumentos posicionais e nomeados em funções
*args (ilimitado de argumentos posicionais)
**kwargs (ilimitado de argumentos nomeados)

Posicional-only Parameters (/) - Tudo antes da barra deve ser APENAS posiconal.
PEP 570 - Python Positional-Only Parameters
https://peps.python.org/pep-0570/

Keyword-Only Parameters (*) - * sozinho NÃO SUGA valores.
  Tudo que vem depois do * deve ser nomeado
PEP 3102 - Keyword-Only Argumets
https://peps.python.org/pep-3102/
'''

# usando *args ofereço a possibilidade de quantidade indefinida e ilimitada de argumentos. A função vai funcionar
#  com um ou vários argumentos. Claro que a lógica da função precisa estar preparada para lidar com isso.
def soma(*args):
    print(sum(args))

soma(1)
soma(1, 2, 3)

# Posicional-Only Parameters
def soma1(a, b, /, x, y):
    print(a + b + x + y)

soma1(1, 2, 3, 4) # a pessoa pode usar tudo posicional para chamar a função
soma1(1, 2, 3, y=4) # ou pode nomear os argumentos que deixei permitido que fossem nomeados (depois da barra)

# Keyword-Only Parameters
def soma2(a, b, *, c):
    print(a + b + c)

soma2(1, 2, c=3) # os dois primeiros argumentos é opcional serem nomeados, mas o terceiro só pode ser nomeado

def soma3(a, b, /, *, c):
    print(a + b + c)

soma3(1, 2, c=3) # agora os dois primeiros argumentos só podem ser posicionais e o último só pode ser nomeado.
