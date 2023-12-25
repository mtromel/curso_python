# video aula 173
# count é um iterador sem fim (itertools)

from itertools import count

c1 = count(8, 8) # posso passar o star e o step
# count é um iterável e é também um iterator:
print('c1', hasattr(c1, '__iter__')) # é iterável?
print('c1', hasattr(c1, '__next__')) # é iterator?

# range é um iterável mas não é um iterator
r1 = range(8, 100, 8)
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)

print()

print('range')
for i in r1:
    print(i)
