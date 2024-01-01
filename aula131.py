'''
video aula 212
@property - um getter no modo Pythônico
getter - um método para obter um atributo
modo pythônico - modo do Python de fazer as coisas
@property é uma propriedade do objeto, ela é um método que se comporta como um atributo
Geralmente é usada nas seguintes situações:
    - como getter
    - para evitar quebrar código cliente
    - para habilitar setter
    - para executar ações ao obter um atributo
Código cliente é o código que usa o seu código.
'''

class Caneta:
    def __init__(self, cor):
        # self.cor = cor
        self.cor_tinta = cor
    
    # uma forma de conseguir mudar um atributo de um método sem quebrar o código cliente é entregando um método que usa o atributo
    # def get_cor(self):
    #     print('GET COR')
    #     return self.cor_tinta
    
    # o modo pythônico de fazer isso é assim:
    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta

# daqui para baixo é o código cliente. Poderia estar em outro módulo

caneta = Caneta('Azul')

# com o recurso de entregar um método que usa o atributo aconteceria assim:
# print(caneta.cor) com a alteração do meu código esse código cliente foi quebrado.
# print(caneta.get_cor()) # esse continua funcionando 

# usando @property não muda nada no código cliente:
print(caneta.cor)
