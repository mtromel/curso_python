'''
video aula 327, 328, 329 e 330
PyPDF2 - Para manipular arquivos PDF
PyPDF é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
extrair texto e imagens, manipular metadados, e mais.
A documentação contém todas as informações necessárias para usar PyPDF2.
Link: https://pypdf2.readthedocs.io/en/3.0.0/
Ative seu ambiente virtual
pip install pypdf2
'''
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'
RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20240621.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

print(len(reader.pages))

for page in reader.pages:
    print(page)
    print()

page0 = reader.pages[0]

print(page0.extract_text())

print(page0.images)
print(len(page0.images))
print(page0.images[0])

imagem0 = page0.images[0]

# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)

writer = PdfWriter()
''' dessa forma crio um novo arquivo só com uma pagina do arquivo original
writer.add_page(page0)

with open(PASTA_NOVA / 'page0.pdf', 'wb') as arquivo:
    writer.write(arquivo)'''

''' dessa forma crio um novo arquivo com as todas as páginas do original
with open(PASTA_NOVA / 'NOVO_PDF.pdf', 'wb') as arquivo:
    for page in reader.pages:
        writer.add_page(page)
    writer.write(arquivo)'''

''' dessa forma separo o arquivo original em arquivos separados de 1 pagina
for i, page in enumerate(reader.pages):
    writer1 = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer1.add_page(page)
        writer1.write(arquivo)
'''

merger = PdfMerger()

files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf',
]

for file in files:
    merger.append(file)

merger.write(PASTA_NOVA / 'MERGED.pdf')
merger.close()
