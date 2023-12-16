'''
video aula 151
try, except, else e finally

Try pode ser usado só com finally, mas nesse caso não está tratando a excessão
Try pode ter quantos except forem necessários
Pode ser usado Try, except, else (sem o finally)
Pode ser usado Try, except apenas
Pode ser usado Try, except, else, finally
Try não pode ficar sozinho

https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
'''

try:
    print('Abriu arquivo')
    8/2
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally: # esse bloco sempre será executado
    print('Fechou arquivo')
    