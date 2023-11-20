'''
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa qubre com 
erros de índices inexistentes na lista.
'''
import os
lista = []
opcao = ''

while opcao != 'sair':
    print('Digite uma opção')
    opcao = input('[i]nserir  [a]pagar  [l]istar: ')

    if opcao == 'i':
        lista.append(input('Valor: '))
        os.system('cls')
    elif opcao == 'a':
        indice_str = input('Escolha um índice para apagar: ')
        try:
            ind = int(indice_str)
            lista.pop(ind)
        except ValueError:
            os.system('cls')
            print('Digite um numero inteiro')
        except IndexError:
            os.system('cls')
            print('Digite um índice válido.')
    elif opcao == 'l':
        os.system('cls')
        if len(lista) > 0:
            for indice, nome in enumerate(lista):
                print(indice, nome)
        else:
            print('Nada para listar')
    elif opcao == 'sair':
        os.system('cls')
        break
    else:
        os.system('cls')
