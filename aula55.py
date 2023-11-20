"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal


# numero_1 = 0.1
# numero_2 = 0.7

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))

'''
a primeira opção é usar o format string como na linha 17. Nesse caso o python retorna uma string formatada com quantas casas decimais 
    eu informar.
a segunda opção é usar o método round. A primeira informação que preciso passar é qual o número quero exibir, a segunda informação é
    quantas casas decimais. Retorna um float.
a terceira opção é importar a biblioteca decimal e usar ela conforme as linhas 13 e 14. Se eu passar o número como float vai continuar
    dando erro. Preciso passar o número como uma string.
'''