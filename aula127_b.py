'''
video aula 206
Exercício - Salve sua classe em JSON
Salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos.
Faça em arquivos separados.
'''
import json

# com esse import não precisa ter criado novamente a constante e a classe.
# from aula127_a import CAMINHO_ARQUIVO, Pessoa

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas)

# na solução do professor ele usou três pessoas no arquivo json. Para importar com mais de um registro precisa usar o índice:
    # p1 = Pessoa(**pessoas[0])
    # p2 = Pessoa(**pessoas[1]) etc...

print(vars(p1))

