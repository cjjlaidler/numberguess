from PySide2 import QtCore, QtWidgets, QtGui


class UsernameWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Username')
        self.username = ''
        self.button = QtWidgets.QPushButton("Submit")
        self.text = QtWidgets.QLabel("Please input a username...")
        self.textbox = QtWidgets.QLineEdit(self)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.setUsername)

    def setUsername(self):
        self.username = self.textbox.text()
        self.close()
