'''
video aula 213
@property + @setter - getter e setter no modo Pythônico
    - como getter
    - para evitar quebrar código cliente
    - para habilitar setter
    - para executar ações ao obter um atributo
Atributos ou métodos que começam com um ou dois underlines não devem ser usados fora da classe.
'''

class Caneta:
    def __init__(self, cor):
        # self.cor = cor
        # self.cor_tinta = cor
        # private protect - estou dizendo para outros desenvolvedores que esse atributo não deve ser usado fora da classe
        # self._cor = cor
        # print('Estou no __INIT__')

        # também posso fazer com que o setter seja sempre executado usando dessa forma
        self.cor = cor

        # nesse atributo estou apenas criando ele sem receber o parametro com a criação da instância
        # o atributo só vai receber valor por meio do método @property e @setter
        self._cor_tampa = None
    
    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor
    
    # para definir um setter uso o mesmo nome do método ponto setter
    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER', valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa' # aqui estou usando o setter. Se não tivesse definido o setter na classe essa linha daria erro.
caneta.cor_tampa = 'Azul'

# getter -> obter valor
print(caneta.cor)
print(caneta.cor_tampa)