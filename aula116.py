'''
video aula 186, 187, 188, 189
Criando arquivos com Python
Usamos a função open para abrir um arquivo (ele pode ou não existir)
    Modos:  r (leitura)
            w (escrita) se o arquivo existir ele limpa o conteúdo do arquivo antes de escrever
            x (para criação)
            a (escreve ao final) append mode - adiciona conteudo ao final do arquivo, sem limpar antes
            b (binário)
            t (modo texto)
            + (leitura e escrita)
context manager - with (abre e fecha)
Métodos úteis:
    write, read (escrever e ler)
    writelines (escrever várias linhas)
    seek (move o cursor)
    readline (ler linha)
    readlines (ler linhas)

Vamos falar mais sobre o módulo os, mas:
    os.remove ou unlink - apaga o arquivo
    os.rename - troca o nome do arquivo

Vamos falar mais sobre o módulo json, mas:
    json.dump - gera o arquivo json
    json.load - 
'''
caminho_arquivo = 'D:\\git\\curso_python\\' # para caminhos do windows precisa incluir mais uma barra para cada barra do caminho
caminho_arquivo += 'aula116.txt'

print(caminho_arquivo)

# arquivo = open(caminho_arquivo, 'r') # dessa forma vai dar problema porque o arquivo ainda não existe

# essa é uma forma de criar o arquivo:
# arquivo = open(caminho_arquivo, 'w') # criando o arquivo
# aqui vou fazer alguma coisa com o arquivo
# arquivo.close()

# essa é outra forma de fazer o mesmo que fiz acima:
with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n') # precisa usar o encoding='utf8' para que palavras acentuadas sejam salvas corretamente
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))
    arquivo.seek(0, 0) # para mudar o cursor para a linha 0 coluna 0
    print(arquivo.read()) # para mostrar na tela o conteúdo do arquivo.
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline()) # ele lê o enter no final da linha do arquivo e executa, por isso pula uma linha
    print(arquivo.readline(), end='') # cada readline é como um next
    print(arquivo.readline().strip()) # o strip elimina os espaços no começo e final, o enter é encarado como espaço

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

print('#' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

with open(caminho_arquivo, 'a+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))

import os

# os.remove(caminho_arquivo)
os.unlink(caminho_arquivo)
# os.rename(caminho_arquivo, 'aula116-2.txt')
# os.unlink('aula116-2.txt')