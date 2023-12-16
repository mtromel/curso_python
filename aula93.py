'''
video aula 149 e 150
Try, except, else e finally
'''

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    print('Linha 1')
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception: # Exception é a classe superior, qualquer erro que não esteja sendo tratado cai aqui
    print('Erro desconhecido')

print('CONTINUAR')
