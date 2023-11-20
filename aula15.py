nome = input('Qual o seu nome? ')
print(f'O seu nome é nome={nome}')
print(f'O seu nome é {nome=}')

# input() sempre gera uma string, então se usarmos para coletar números podemos ter problemas em operações matemáticas
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

print(f'A soma dos números é: {numero_1 + numero_2}')

# para converter para número precisamos usar int(), mas dessa forma abaixo não é recomendado porque se o usuário digitar uma letra vai
# quebrar nosso programa na conversão.
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

print(f'A soma dos números é: {numero_1 + numero_2}')

# uma forma de resolver esse problema é converter para int() depois de coletar, o que possibilita antes de rodarmos o código de conversão
# fazermos uma checagem se o que o usuário digitou é número mesmo ou não

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

# a checagem entraria aqui, antes da conversão. Do jeito que está o código quebra nas linhas abaixo caso seja digitado letra

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')