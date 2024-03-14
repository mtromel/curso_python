'''
video aula 307
argparse.ArgumentParser para argumentos mais complexos
Tutorial oficial:
https://docs.python.org/pt-br/3/howto/argparse.html
'''
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra olá mundo na tela',
    # type=str,  # Tipo do argumento
    metavar='String',
    # default='Olá mundo',  # Valor padrão
    required=False,
    action='append',  # Recebe o argumento mais de uma vez
    # nargs='+'  # Recebe mais de um valor
    )

parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true'  # retorna true se tiver sido chamado
    )

args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de basic')
    print(args.basic)
else:
    print('O valor de basic: ', args.basic)

print(args.verbose)
