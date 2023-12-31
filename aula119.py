'''
video aula 192, 193
Exercício - Lista de taferas com desfazer e refazer
Música para codar =)
Everybody wants to rule the world - Tears for fears
todo = [] -> lista de tarefas
todo = ['fazer café] -> adicionar fazer café
todo = ['fazer café', 'caminhar'] -> adicionar caminhar
desfazer = ['fazer café'] -> refazer['caminhar']
desfazer = [] -> refazer['caminhar', 'fazer café']
refazer = todo['fazer café]
refazer = todo['fazer café', 'caminhar']

Rubber duck debugging (Debug com Pato de Borracha)
'''
import os
import json

def salva_json(tarefas, nome_arquivo):
    dados = tarefas
    with open(nome_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)
    return dados

def ler_json(tarefas, nome_arquivo):
    dados = []
    try:
        with open(nome_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salva_json(tarefas, nome_arquivo)
    return dados


def listar(lista):
    print()
    print('TAREFAS')
    if not lista:
        print()
        print('Nada a listar')
        print()
        return
    
    print(*lista, sep='\n')
    print()


CAMINHO_ARQUIVO = 'aula119.json'
todo = ler_json([], CAMINHO_ARQUIVO)
refazer = []

while True:
    print('Comandos: listar, desfazer, refazer, sair')
    entrada = input('Digite uma tarefa ou comando: ').lower()

    if entrada == 'listar':
        listar(todo)
    elif entrada == 'desfazer':
        if bool(todo) is False:
            print()
            print('Nada a desfazer')
            print()
        else:            
            ultimo_valor = todo.pop()
            refazer.append(ultimo_valor)
            salva_json(todo, CAMINHO_ARQUIVO)
            listar(todo)
    elif entrada == 'refazer':
        if bool(refazer) is False:
            print()
            print('Nada a refazer')
            print()
        else:
            ultimo_valor = refazer.pop()
            todo.append(ultimo_valor)
            salva_json(todo, CAMINHO_ARQUIVO)
            listar(todo)
    elif entrada == 'sair':
        break
    elif entrada == 'clear':
        os.system('cls')    
    else:
        todo.append(entrada)
        salva_json(todo, CAMINHO_ARQUIVO)
        listar(todo)