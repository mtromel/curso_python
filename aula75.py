'''
video aula 117 e 118
Exercícios

Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro
'''

# import os

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

# while True:
#     numero = input('Digite um número: ')
    
#     try:
#         numero_inteiro = int(numero)
#         acao = input('Digite [d] para Duplicar, [t] para Triplicar ou [q] para Quadruplicar o número: ').lower()
#         if acao == 'd':
#             print(duplicar(numero_inteiro))
#         elif acao == 't':
#             print(triplicar(numero_inteiro))
#         elif acao == 'q':
#             print(quadruplicar(numero_inteiro))
#         elif acao == 'sair':
#             break
#         else:
#             os.system('cls')
#             continue
#     except:
#         os.system('cls')
#         print('Digite um número inteiro')
    
# solução do professor:
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
    
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

    


