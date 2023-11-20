'''
Operadores lógicos
and (e) or (ou) not (não)
and - Todas as condições precisam ser verdadeiras
    Se qualquer valor for considerado falso, a expressao inteira será avaliada naquele valor.
or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
    Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
São consideradas falsy (que vc  já viu) 0 0.0 '' False
Também existe o tipo None que é usado para representar um não valor
'''

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')



# avaliação de curto circuito
print(True and 0 and True)
print(True or False)
senha = input('Senha: ') or 'Sem senha'
print(senha)

if 1 and 1:
    print(True and 1 and False)
