from PySide2 import QtCore, QtWidgets, QtGui

class GameWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 300)
        self.setWindowTitle('Number Guess')
        self.menubar = QtWidgets.QMenuBar(self)
        self.fileMenu = self.menubar.addMenu('File')
        def start_new_game(self):
        	print('start game')
        self.newGame = QtWidgets.QAction('New Game', self)
        self.newGame.setShortcut('Ctrl+N')
        self.newGame.setStatusTip('Start a new game')
        self.newGame.triggered(start_new_game(self))


        self.fileMenu.addAction(self.newGame)
       
        self.username = ''
        self.text = QtWidgets.QLabel('Welcome to Number Guess')
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.setLayout(self.layout)

