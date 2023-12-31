'''
video aula 191
Problema dos parãmetros mutáveis em funções Python

Toda vez que eu for criar parametros em funções Python tenho que checar se o parãmetro é mutável.
    Se for mutável não colocar valor padrão na função. Sempre fazer None e dentro da função criar o valor do
    parâmetro se não for enviado o parâmetro

Na função adiciona clientes se criar ela assim teremos um problema:
def adiciona_clientes(nome, lista=[]):
    ...

Teremos um problema porque ao chamar a função a primeira vez sem informar a lista como abaixo o Python cria a lista no escopo
    da função. Ao criar a cliente2 o Python iria mesclar as duas listas. Por isso que preciso colocar o parâmetro como padrão
    None e usar um if para verificar se não foi passada nenhuma lista. Assim o Python só cria  lista uma vez.
'''

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Marcos')
adiciona_clientes('Angela', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
