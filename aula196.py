# video aula 324
# threads podem ser usadas para processos que podem demorar muito para
# executar e isso vai travar a interface gráfica. Para evitar isso é só
# criar uma classe como abaixo e fazer ela executar o processo demorado.
from time import sleep
from threading import Thread
from threading import Lock


# class MeuThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo

#         super().__init__()

#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)


# t1 = MeuThread('Thread 1', 2)
# t1.start()

# t2 = MeuThread('Thread 2', 4)
# t2.start()

# t3 = MeuThread('Thread 3', 6)
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(1)

# video aula 325 - outra forma de criar threads
# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)

# t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
# t1.start()

# t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
# t2.start()

# t2 = Thread(target=vai_demorar, args=('Olá mundo 3!', 2))
# t2.start()

# for i in range(20):
#     print(i)
#     sleep(.5)


# t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 10))
# t1.start()
# t1.join()
# usando o join o efeito é o mesmo que o while, mas o programa fica
# bloqueado até que a thread termine para só então  executar o
# print que está abaixo do while. Nesse caso não preciso do while.

# while t1.is_alive():
#     print('Esperando a thread')
#     sleep(2)

# print('Thread acabou')

# video aula 326

# Nesse exemplo abaixo conseguimos simular um problema que pode ocorrer ao usar
# threads. Na classe ingressos, se comentar as linhas de lock e sleep o código
# continua funcionando. Se deixar a linha de sleep sem comentar o código dá
# erro de estoque porque todo o for vai passar pela validação do if da classe
# antes de reduzir o estoque. Com o lock é como se trancasse a classe até que
# cada thread termine.

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque.')

        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)
