'''
video aula 156
recarregar módulos - importlib.reload
singleton - só pode existir uma instância daquilo no programa que estou executando
'''
import importlib
import aula98_m

print(aula98_m.variável)

for i in range(10):
    importlib.reload(aula98_m)
    print(i)
    

print('Fim')
