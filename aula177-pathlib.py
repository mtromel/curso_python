'''
video aula 291 link para o canal do youtube
https://youtu.be/T17BTNKBeJY
pathlib
Usamos a pathlib para trabalhar com caminhos, pastas e arquivos de forma
  que um código funcione em Windows, Linux e Mac.
'''
from pathlib import Path


caminho_projeto = Path()
print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
print(caminho_arquivo)
print(caminho_arquivo.parent)
print(caminho_arquivo.parent.parent)
print('-----------------')
ideias = caminho_arquivo.parent / 'ideias'
print(ideias / 'arquivo.txt')

print('------------------')
arquivo = Path.home() / 'Documents' / 'arquivo.txt'
arquivo.touch()  # cria o arquivo
# print(arquivo)

arquivo.write_text('')
with arquivo.open('a+') as file:
    file.write('Uma linha\n')
    file.write('Outra linha\n')

print(arquivo.read_text())

arquivo.unlink()  # apaga o arquivo

caminho_pasta = Path.home() / 'Documents' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)  # cria a pasta, se já existe ignora
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Hey')

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá mundo\n')
        text_file.write(f'file_{i}.txt')

# o código abaixo faz a mesma coisa que o shutil rmtree


def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink()

    if remove_root:
        root.rmdir()


rmtree(caminho_pasta)
