'''
video aula 298
string.Template para substituir variáveis em textos
doc: https://docs.python.org/3/library/string.html#template-strings
Métodos:
substitute: substitui mas gera erros se faltar chaves
safe_substitute: substitui sem gerar erros
Você também pode trocar o delimitador e outras coisas criando uma subclasse
de template.
'''
import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula183.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float | int) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)


# se eu quiser usar um delimitador diferente preciso criar uma classe
class MyTemplate(string.Template):
    delimiter = '%'


# para usar o delimitador padrão no lugar de MyTemplate uso o string.template
    # o delimitador padrão é o $
with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()
    template = MyTemplate(texto)
    print(template.substitute(dados))
