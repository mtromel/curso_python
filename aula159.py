'''
video aula 265, 266, 267, 268, 269, 270
dataclasses - o que são dataclasses?
O módulo dataclasses fornece um decorador e funções para criar métodos como
    __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
    usuário.
Em resumo: dataclasses são syntax sugar para criar classes normais.
Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
doc: https://docs.python.org/3/library/dataclasses.html
'''
# from dataclasses import dataclass, asdict, astuple


# para que o Python não crie o __init__ nessa dataclass poderia fazer assim:
# @dataclass(init=False)
# nesse caso precisaria criar o __init__ e o __post_init__ não iria funcionar

# outro método que posso usar na data class é o frozen:
# @dataclass(frozen=True)
# isso congela a classe e não aceita mais nenhuma nova instância. Para ela
# continuar funcionando precisa comentar ou excluir o __post_init__

# outro método interessante é o order=True. Ele permite usar o sorted para
# ordenar uma lista da classe por exemplo.
# @dataclass
# class Pessoa:
#     nome: str
#     sobrenome: str

# o post init é executado logo após o init. Se não tiver o init não
# executa o post init
# def __post_init__(self):
#     self.nome_completo = f'{self.nome} {self.sobrenome}'

# @property
# def nome_completo(self):
#     return f'{self.nome} {self.sobrenome}'

# @nome_completo.setter
# def nome_completo(self, valor):
#     nome, *sobrenome = valor.split()
#     self.nome = nome
#     self.sobrenome = ' '.join(sobrenome)


# if __name__ == '__main__':
#     p1 = Pessoa('Luiz', 'Otávio')
#     p2 = Pessoa('Luiz', 'Otávio')
#     print(p1)
#     # print(p1.nome_completo)
#     print(p2)
#     print(p1 == p2)
#     print(asdict(p1).keys())
#     print(asdict(p1).values())
#     print(asdict(p1).items())
#     print(astuple(p2))

# video aula 270
from dataclasses import dataclass, field, fields

# se eu quisesse criar uma classe com valores default e precisasse de um dict
# preciso usar o método field de dataclasses, com default_factory
# o fields mostra todos os métodos e como estão configurados na classe.


@dataclass
class Pessoa:
    nome: str = 'Missing'
    sobrenome: str = 'Not Sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    print(fields(p1))
    print(p1)
