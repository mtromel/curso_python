import sys
from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QMainWindow, QApplication
from window import Ui_MainWindow
from typing import cast


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.buttonSend.clicked.connect(self.changeLabelResult)

        self.LineName.installEventFilter(self)
    
    def changeLabelResult(self):
        text = self.LineName.text()
        self.labelResult.setText(text)
    

    # esse é uma função do PySide6 que permite alterar o que acontece na gui
    # sem alterar o arquivo gerado pelo QtDesigner
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:

        if event.type() == QEvent.Type.KeyPress:
            # tenho certeza que o tipo é KeyPress
            event = cast(QKeyEvent, event)
            text = self.LineName.text()
            self.labelResult.setText(text + event.text())

        return super().eventFilter(watched, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()