'''
video aula 341
QApplication e QPushButton de PySide6.QtWidgets
QApplication -> O Widget principal da aplicação
QPushButton -> Um botão
PySide6.QtWidgets -> Onde estão os widgets do PySide6
'''
import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px; color: red;')
botao.show()  # Adicionar o widget na hierarquia e exibe a janela

botao2 = QPushButton('Botão 2')
botao2.show()

app.exec()  # Executa o loop da aplicação

# com o código dessa forma vou ter duas janelas abertas, porque o QApplication
# vai executar cada widget em uma janela.