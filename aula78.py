'''
video aula 126
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.html
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.
'''

# Criando um set:
# set(iteravel) ou {1, 2, 3}
s1 = set() # cria um set vazio
print(s1, type(s1))
s1 = set('Luiz') # se eu inserir um texto dessa forma o set vai iterar sobre o texto
print(s1) # não garante a ordem, ou seja pode ser armazenado fora de ordem.
s1 = {'Luiz', 1, 2, 3} # também pode ser criado dessa forma
print(s1, type(s1))


'''
video aula 127
Sets são eficientes para remover valores duplicados de iteráveis.
- seus valores serão sempre únicos;
- não aceitam valores mutáveis (lista, dicionarios);
- eles não tem indexes;
- eles não garantem ordem;
- eles são iteráveis (for, in, not in)
'''

s1 = {1, 2, 3, 3, 3, 3, 3, 1} # o set elimina naturalmente todos os valores duplicados.
print(s1)

# o set é muito eficiente para remover valores duplicados.
# exemplo tenho uma lista ou uma tupla como abaixo
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1) # converto a lista para um set. Automaticamente os números duplicados são descartados.
l2 = list(s1) # agora converto o set em lista novamente. Com isso tenho uma lista sem valores duplicados.
print(l2)

# um problema dessa conversão é que o set não garante a ordem.

'''
video aula 128
Métodos úteis:
add, updte, clear, discard
'''
s1 = set()
s1.add('Luiz')
s1.add(1) # envia um valor de cada vez
s1.update('Olá mundo') # se passar só assim ele vai iterar sobre a string e armazenar como letras
s1.update(('Olá mundo', 1, 2, 3, 4)) # pode ser usado para enviar vários valores
# s1.clear() # limpa o set
s1.discard('Olá mundo') # descarta o valor informado
s1.discard('Luiz')
print(s1)

'''
video aula 129
Operadores úteis:
união | união (union) - Une
intersecção & (intersection) - itens presentes em ambos
diferença - itens presentes apenas no set da esquerda
diferença simétrica ^ - itens que não estão em ambos
'''

s1 = {1, 2, 3}
s2 = {2, 3, 4}
# s3 = s1 | s2 # união
# s3 = s1 & s2 # intersecção
# s3 = s1 - s2 # diferença
s3 = s1 ^ s2 # diferença simétrica

print(s3)
