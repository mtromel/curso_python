'''
video aula 256
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar / depositar nessa conta. Contas corrente tem um limite extra.

Conta(ABC)
    ContaCorrente
    ContaPoupança

Pessoa(ABC)
    Cliente
        Cliente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupança)
Criar classes ContaPoupança e ContaCorrente que herdam de conta
    ContaCorrente deve ter um limite extra
    Contas tem agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
'''

from classes import Banco, ContaCorrente, ContaPoupanca, Cliente, Agencia

itau = Banco('Itau')
ag001_itau = Agencia('001')
itau.agencia = ag001_itau
cliente1 = Cliente('Marcos', '46')
itau.cliente = cliente1
cc1234_ag001_itau = ContaCorrente(ag001_itau, '1234-4')
cp1234_ag001_itau = ContaPoupanca(ag001_itau, '1234-500')

cc1234_ag001_itau.depositar(500)
cp1234_ag001_itau.depositar(1000)
cc1234_ag001_itau.sacar(100)
cc1234_ag001_itau.sacar(200)
cc1234_ag001_itau.sacar(300)
cc1234_ag001_itau.sacar(100)
cc1234_ag001_itau.sacar(50)
cp1234_ag001_itau.sacar(600)
cp1234_ag001_itau.sacar(401)
