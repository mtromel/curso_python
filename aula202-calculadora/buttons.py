from typing import TYPE_CHECKING
import math
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber, convertToNumber

if TYPE_CHECKING:
    from display import Display
    from main_window import MainWindow
    from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        # às vezes quando define assim perde o estilo anterior, tomar cuidado.
        # self.setStyleSheet(f'font-size {MEDIUM_FONT_SIZE}px;')

        # outra forma de fazer isso sem sobrescrever o style:
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        # font.setItalic(True)
        # font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        # self.setCheckable(True)
        

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', 
                 window: 'MainWindow', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Sua conta'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()
    
    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertToDisplay, buttonText)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)
    
    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)
        
        if text == '◀':
            self._connectButtonClicked(button, self.display.backspace)

        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)
        
        if text in '+-/*^':
            self._connectButtonClicked(
                button, 
                self._makeSlot(self._configLeftOp, text)
                )

        if text == '=':
            self._connectButtonClicked(button, self._eq)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return
        
        number = convertToNumber(displayText) * -1
        self.display.setText(str(number))

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)
        self.display.setFocus()
    
    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # limpa o display
        self.display.setFocus()

        # Se a pessoa clicou no operador sem configurar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            self._showError('Você não digitou nada')
            return
        
        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = convertToNumber(displayText)
        
        self._op = text
        self.equation = f'{self._left} {self._op} ??'
    
    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._showError('Conta incompleta.')
            return

        self._right = convertToNumber(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, int | float):
                result = math.pow(self._left, self._right)
                result = convertToNumber(str(result))
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Divisão por zero.')
        except OverflowError:
            self._showError('Essa conta não pode ser realizada.')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
        self.display.setFocus()

        if result == 'error':
            self._left = None

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()

        # msgBox.setInformativeText('Texto de qualquer tamanho aqui')

        # usando vários botões e mudando o texto do botão
        # msgBox.setStandardButtons(
        #     msgBox.StandardButton.NoToAll |
        #     msgBox.StandardButton.Ok
        # )

        # msgBox.button(msgBox.StandardButton.NoToAll).setText('Não para todos')

        # usando vários botões e identificando qual o botão clicado
        # msgBox.setStandardButtons(
        #     msgBox.StandardButton.Ok |
        #     msgBox.StandardButton.Cancel |
        #     msgBox.StandardButton.Save
        # )

        # result = msgBox.exec()

        # if result == msgBox.StandardButton.Ok:
        #     print('Usuário clicou em OK')
        # elif result == msgBox.StandardButton.Cancel:
        #     print('Usuário clicou em Cancel')
        # elif result == msgBox.StandardButton.Save:
        #     print('Usuário clicou em Save')

    def _showInfo(self, text):
            msgBox = self._makeDialog(text)
            msgBox.setIcon(msgBox.Icon.Information)
            msgBox.exec()
            self.display.setFocus()