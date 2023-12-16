'''
video aula 147
Introdução as Generator functions em Python
generator = (n for n in range(1000000))
'''

def generator(n=0, maximum=10):
    # yield 1 # pausar
    # print('Continuando...')
    # yield 2 # pausar
    # print('Mais uma...')
    # yield 3 
    # print('Vou terminar')
    # return 'ACABOU'
    while True:
        yield n
        n += 1
        if n >= maximum:
            return

# gen = generator(n=0)
# gen = generator()
gen = generator(n=5, maximum=8)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)
