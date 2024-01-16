'''
video aula 231
Polimorfismo em Python Orientado a Objetos

Polimorfismo é o principio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais (com mesma
    assinatura) mas comportamentos diferentes.

Assinatura do método = Mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura)

Opinião + principios que contam:
Assinatura do método: nome, parâmetros e retorno iguais
SO"L"ID
Princípio da substituição de liskov
    Objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação.

Sobrecarga de métodos (overload) - Python não suporta
Sobreposição de métodos (override) - Python suporta
'''
from abc import ABC, abstractmethod

class Notificacao:
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True

class NotificaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando -', self.mensagem)
        return False

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')

notificacao_email = NotificacoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificaoSMS('testando SMS')
notificar(notificacao_sms)



# n = NotificaoSMS('testando notificação')
# n.enviar()

