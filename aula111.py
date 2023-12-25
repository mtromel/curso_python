'''
video aula 176
map - para mapear dados
'''

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

novos_produtos = [
    {**p, 'preco': aumentar_porcentagem(p['preco'], 1.1)} for p in produtos
]

print_iter(produtos)
print_iter(novos_produtos)

# existe um módulo em Python que são ferramentas para funções
# uma ferramenta é a partial, é uma função que vai receber uma função, um ou vários argumentos da função

from functools import partial

# para fazer o aumento dos preços em 10% como feito acima pode ser feito dessa forma:

aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)
novos_produtos = [
    {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
]

print_iter(novos_produtos)

# map substitui o list comprehension mas ele precisa receber uma função

def muda_preco_de_produtos(produto):
    return { **produto, 'preco': aumentar_dez_porcento(produto['preco'])}

novos_produtos = map(muda_preco_de_produtos, produtos)