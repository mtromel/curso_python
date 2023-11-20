'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
'''
nome = input('Digite o seu primeiro nome: ')

tam = len(nome)

if tam > 1:
    if tam <= 4:
        print('Seu nome é curto')
    elif tam > 4 and tam < 7:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de um caractere')