'''
video aula 145 e 146
Generator expression, Iterables e Iterators em Python

O iterável tem a responsabilidade de ter os valores sequencialmente
O iterator só tem a responsabilidade de entregar um valor por vez. Só sabe quem o próximo valor, não sabe quem é o
    primeiro, quem o anterior, quem é o último, não sabe o tamanho do iterável.
Generator são funções que sabem pausar em determinada ocasião. É também um iterator. Não sabe mais nada além do próximo
    valor.
'''
import sys

iterable = ['Eu', 'tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__

# o iterável salva todos os valores na memoria quando é criado
lista = [n for n in range(10000)]

# o generator não criou todos os valores na memória ainda, vai criar um por vez conforme formos pedindo.
generator = (n for n in range(10000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))
print(sys.getsizeof(generator))
