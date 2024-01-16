'''
video aula 233, 234, 235
Criando Exceptions em Python Orientado a Objetos
Para criar uma exception em Python você só precisa herdar de alguma excessão da linguagem.

A recomendação da doc é herdar de Exception.
htts://docs.python.org/3/library/exceptions.html

Criando exceções (comum colocar Error ao final)
Levantando (raise) / Lançando (throw) exceções
Relançando exceções
Adicionando notas em exceções (3.11.0)
'''
class MeuError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('olha a nota 1')
    exception_.add_note('você errou isso')
    raise exception_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo') # relançando a exceção
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    raise exception_ from error

# levantar()