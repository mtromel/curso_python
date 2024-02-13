'''
video aula 287
os + shutil - Apagando e copiando pastas com Python
Vamos copiar arquivos de uma pasta para outra.
Copiar -> shutil.copy
Copiar Arvore recursivamente -> shutil.copytree
Apagar Arvore recursivamente -> shutil.rmtree
Apagar arquivos -> os.unlink
Renomear / Mover -> shutil.move or os.rename
'''
import os
import shutil

HOME = os.path.expanduser('~')  # pega a home desse usuário
DOCUMENTOS = os.path.join(HOME, 'Documents')
PASTA_ORIGINAL = os.path.join(DOCUMENTOS, 'Exemplo')
NOVA_PASTA = os.path.join(DOCUMENTOS, 'Nova_pasta')

shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.rmtree(NOVA_PASTA, ignore_errors=True)  # atenção: não vai p/ lixeira


# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
#         )
#         os.makedirs(caminho_novo_diretorio, exist_ok=True)

#     for file_ in files:
#         caminho_arquivo = os.path.join(root, file_)
#         caminho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file_
#         )
#         shutil.copy(caminho_arquivo, caminho_novo_arquivo)
