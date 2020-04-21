from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QObject, SIGNAL


class GameWindow(QtWidgets.QWidget):

	def __init__(self, game, gameMessage):
		super().__init__()
		self.setMinimumSize(200, 300)
		self.setWindowTitle('Number Guess')
		menubar = QtWidgets.QMenuBar(self)
		fileMenu = menubar.addMenu('File')

		def start_new_game():
			game.run()

		newGame = QtWidgets.QAction('New Game', self)
		newGame.setShortcut('Ctrl+N')
		newGame.setStatusTip('Start a new game')
		QObject.connect(newGame, SIGNAL('triggered()'), start_new_game)

		fileMenu.addAction(newGame)

		username = ''
		gameMessage.setAlignment(QtCore.Qt.AlignCenter)
		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(gameMessage)
		self.setLayout(layout)
