'''
video aula 294
csv.reader e csv.DictReader
csv.reader lê o CSV em formato de lista
csv.DictReader lê o CSV em formato de dicionário
'''

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

# para escrever em arquivo CSV usando um dicionário
lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av. 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )

    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)


# para escrever em um arquivo CSV usando uma lista
# lista_clientes = [
#     ['Luiz Otávio', 'Av. 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]

# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)
#         # print(cliente.values())
#         # escritor.writerow(cliente.values())
