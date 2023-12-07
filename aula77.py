'''
video aula 124
Exercício - sistema de perguntas e respostas
'''

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '5', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

tamanho_lista_perguntas = len(perguntas)
lista_perguntas_indice = 0
acertos = 0

while lista_perguntas_indice < tamanho_lista_perguntas:
    pergunta_atual = list(perguntas[lista_perguntas_indice])
    print(f'{pergunta_atual[0]}: {perguntas[lista_perguntas_indice]["Pergunta"]}')
    print()
    print(f'{pergunta_atual[1]}:')

    indice = 0
    for valor in perguntas[lista_perguntas_indice]['Opções']:
        print(f'{indice}) {valor}')
        if valor == perguntas[lista_perguntas_indice]['Resposta']:
            resposta_certa = str(indice)
        indice += 1
    resposta = input('Escolha uma opção: ')
    if resposta == resposta_certa:
        print('Acertou!! 👍')
        acertos += 1
    else:
        print('Errou!! ❌')
    print()
    lista_perguntas_indice += 1

print('Você acertou ', acertos)
print(f'de {tamanho_lista_perguntas} perguntas.')

# solução do professor


qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')