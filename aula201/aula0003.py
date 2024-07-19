'''
video aula 342
QWidget e QLayout de PySide6.QtWidgets
QWidget -> genérico
QLayout -> Um widget de layout que recebe outros widgets

Resumo: para que eu tenha varias coisas em uma janela, tenho que ter um
  widget central, esse widget central tem que ter um layout, o layout posso
  escolher qual o layout eu quiser (vertical, horizontal, grid, etc...). Para
  adicionar coisas no central widget basta adicionar coisas no layout. Poderia
  ter outro layout dentro do layout.
'''
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px; color: red;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px; color: blue;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px; color: blue;')

central_widget = QWidget()
# layout = QVBoxLayout()  # mostra o layout na vertical
# layout = QHBoxLayout()  # mostra o layout na horizontal
layout = QGridLayout()  # mostra o layout em grid
central_widget.setLayout(layout)

# layout.addWidget(botao)
# layout.addWidget(botao2)

# para usar o layout em grid posso informar outros dados
layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


central_widget.show()  # Central Widget entre na hierarquia e mostre sua janela
app.exec()  # Executa o loop da aplicação