'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local
O escopo global é o escopo é o escopo onde todo o código é alcançável
Escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados
Não temos acesso a nomes de escopos internos nos escopos externos
A palavra global faz uma variavel de escopo externo ser a mesmo no escopo interno
'''

x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)
    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)