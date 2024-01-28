'''
video aula 271
namedtuples - tuplas imutáveis com nomes para valores
Usamos namedtuples para criar classes de objetos que são apenas um
    agrupamento de atributos, como classes normais sem métodos, ou registros
    de bases de dados, etc.
As namedtuples são imutáveis assim como as tuplas.
https://docs.python.org/3/library/collections.html#collections.namedtuple
https://docs.python.org/3/library/typing.html#typing.NamedTuple
'''
# from collections import namedtuple


# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR', 'NAIPE']
# )

# outra forma de fazer a mesma coisa, usando typing:
from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


as_espadas = Carta('A', 'espadas')
print(as_espadas)
print(as_espadas[0])
print(as_espadas.valor)
print(as_espadas[1])
print(as_espadas.naipe)

print()
print(as_espadas._fields)
print(as_espadas._field_defaults)
print(as_espadas._asdict())

print()
for valor in as_espadas:
    print(valor)
