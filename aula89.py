'''
video aula 144
dir, hasattr e getattr em Python

no debug console posso usar:
dir(string) -> retorna todos os atributos disponíveis dentro da string, ou do objeto que eu informar
hasattr -> checa se um determinado objeto tem um determinado atributo lá dentro.
getattr -> pega o método
'''

string = 'Luiz'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())

if hasattr(string, metodo):
    print('Existe', metodo)
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)