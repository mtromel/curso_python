'''
video aula 179 e 180
Funções recursivas e recursividade
    - funções que podem se chamar de volta
    - úteis para dividir problemas grandes em partes menores
Toda função recursiva deve ter:
    - Um problema que possa ser dividido em partes menores
    - Um caso recursivo que resolve o pequeno problema
    - um caso base que para a recursão
    - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120
https://brasilescola.uol.com.br/matematica/fatorial.htm
'''
def recursiva(inicio=0, fim=10):
    
    print(inicio, fim)
    
    # Caso base
    if inicio >= fim:
        return fim

    # Caso recursivo = contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))
# print(factorial(1000)) # esse código gera erro por estoura a stack