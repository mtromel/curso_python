'''
video aula 343
QMainWindow e centralWidget
-> QApplication (app)
    -> QMainWindow (window->setCentralWidget)
        -> CentralWidget (central_widget)
            -> Layout (layout)
                -> Widget 1 (botao1)
                -> Widget 2 (botao2)
                -> Widget 3 (botao3)
    -> show
-> exec
'''
import sys
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QGridLayout, 
                               QMainWindow)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita')

def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')

botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 80px; color: red;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px; color: blue;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px; color: blue;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Qualquer coisa')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(lambda: slot_example(status_bar))

window.show()
app.exec()  # Executa o loop da aplicação