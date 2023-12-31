'''
video aula 206
Exercício - Salve sua classe em JSON
Salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos.
Faça em arquivos separados.
'''
import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 35)

with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(p1.__dict__, arquivo, ensure_ascii=False, indent=2)