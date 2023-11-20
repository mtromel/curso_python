'''
Calculadora com while
'''
while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+-/*): ')
    operacao = 0
    num_1_float = 0
    num_2_float = 0
    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        operacao = num_1_float + num_2_float
    elif operador == '-':
        operacao = num_1_float - num_2_float
    elif operador == '/':
        operacao = num_1_float / num_2_float
    elif operador == '*':
        operacao = num_1_float * num_2_float
    
    print(f'O resultado da operação {numero_1} {operador} {numero_2} = {operacao}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break