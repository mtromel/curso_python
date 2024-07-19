'''
video aula 338, 339, 340
PySide6 para GUI (interface gráfica) com Qt em Python - Instalação
- A seção original desse curso usou PyQt5 (estamos atualizando para PySide6)
- Essas bibliotecas (PySide e PyQt) usam a biblioteca Qt
- Qt é uma biblioteca usada para a criação de GUI (Interface gráfica
  do usuário) escrita em C++.
  - PySide e PyQt conseguem fazer a ponte (binding) entre o Python e a
  blibioteca para a criação de interfaces gráficas sem  ter que usar outra
  linguagem de programação.
- PySide6 é uma referencia à versão 6 da Qt (Qt 6)
- Qt é multiplataforma, ou seja, deve funcionar em Windows, Linux e Mac.

Por que mudei de PyQt para PySide na atualização?
- PySide foi desenvolvido pela The Qt Company (da Nokia), como parte do
  projeto Qt for Python project - https://doc.qt.io/qtforpython/
- Por usarem a mesma biblioteca (Qt), PySide e PyQt são extremamente
  similares, muitas vezes os códigos são idênticos. Portante mesmo que você
  ainda queira usar PyQt, será muito simples portar os códigos. Muitas vezes
  basta trocar o nome de PySite para PyQt e vice-versa.
- A maior diferença entre PyQt e PySide está na licença:
  PyQt usa GPL ou commercial e PySide usa LGPL.
  Em resumo: com PySide, você tem a permissão de uso da biblioteca para fins
  comerciais, sem ter que compartilhar o código escrito por você para o
  público.
  Licenças são tópicos complexos, portanto, se oriente sobre elas
  antes de usar qualquer software de terceiros.
  https://tldrlegal.com/license/gnu-lesser-general-public-licence-v3-(lgpl-3)

Para instalar:
ativar o ambiente virtual
    .\venv\Scripts\activate
instalar
    pip install pyside6

'''
import PySide6.QtCore

# Prints PySide6 version
print(PySide6.__version__)

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)
