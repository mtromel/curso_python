
'''
Introdução ao desempacotamento
'''
# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes
#  nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
nome1, *resto = ['Maria', 'Helena', 'Luiz']

#  tem uma convenção entre os dev python que se eu não quero usar uma variável nomeio ela com _, por exemplo: ao invés de *resto fica *_
print(nome1, resto)