'''
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
Operadores de atribuição
= += -= *= /= //= **= %=
'''

contador = 0

while contador < 100:
    contador += 2

    if contador == 6:
        print('Não vou mostrar o 6')
        continue  # volta para o inicio do laço

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o ,', contador)
        continue

    print(contador)

    if contador == 40:
        break  # quebra o laço

print('Acabou')