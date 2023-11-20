'''
Operadores in e not in
Strings são iteráveis
 0 1 2 3 4 5
 M a r c o s
-6-5-4-3-2-1
'''
nome = 'Marcos'
print(nome[2])
print(nome[-4])

print('a' in nome)
print('z' in nome)
print(10 * '-')
print('Mar' not in nome)
print('z' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')