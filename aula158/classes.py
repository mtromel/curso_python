from abc import ABC, abstractmethod


class Banco():
    def __init__(self, nome):
        self.nome = nome
        self._agencia = None
        self._conta = None
        self._cliente = None

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, nome):
        self._agencia = nome

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, nome):
        self._conta = nome

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, nome):
        self._cliente = nome

    def autentica(self, ag, clt, cta):
        if self._agencia == ag & self._cliente == clt & self._conta == cta:
            return True
        return False


class Agencia:
    def __init__(self, ag):
        self.agencia = ag


class Conta(ABC):
    def __init__(self, agencia, conta):
        self._agencia = agencia
        self._conta = conta
        self._saldo = 0

    def saldo(self):
        return self._saldo

    def atualizar_saldo(self, valor):
        self._saldo = valor

    def depositar(self, valor):
        self._saldo += valor
        print('Depósito realizado com sucesso! Seu saldo é R$ ', self._saldo)

    @abstractmethod
    def sacar(self): ...


class ContaCorrente(Conta):
    def __init__(self, agencia, conta):
        super().__init__(agencia, conta)
        self._cliente = None
        self._limite = 200

    # @property
    # def limite(self):
    #     return self._limite

    # @limite.setter
    # def limite(self, valor):
    #     self._limite = valor

    def sacar(self, valor):
        sld = super().saldo()
        saldo_total = sld + self._limite

        if not Banco.autentica(self, Banco.agencia, Banco.cliente,
                               Banco.conta):
            return print('Saque não permitido pelo Banco')

        if valor <= saldo_total:
            sld = sld - valor
            self.atualizar_saldo(sld)
            print('Saque realizado com sucesso! Seu saldo é R$ ',
                  super().saldo())
        else:
            print('Saldo insuficiente. Seu saldo é R$ ', super().saldo(),
                  'e seu limite é R$ ', self._limite)


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta):
        super().__init__(agencia, conta)

    def sacar(self, valor):
        sld = super().saldo()

        if valor <= sld:
            sld = sld - valor
            self.atualizar_saldo(sld)
            print('Saque da poupança realizado com sucesso! Seu saldo é R$ ',
                  super().saldo())
        else:
            print('Saldo insuficiente. Seu saldo é R$ ', super().saldo())


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta_corrente = False
        self._conta_poupanca = False
