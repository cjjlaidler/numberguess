from PySide2 import QtCore, QtWidgets, QtGui

class GameWindow(QtWidgets.QWidget):

    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle('Number Guess')
        self.username = ''
        self.text = QtWidgets.QLabel('Welcome to Number Guess')
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.setLayout(self.layout)

