import sys
from Models.Game import Game
from Models.Guess import Guess
from Models.PreviousGuesses import PreviousGuesses
from Models.Highscores import Highscores
from Models.Difficulty import Difficulty
from ui.UsernameWindow import UsernameWindow
from ui.GameWindow import GameWindow
from PySide2 import QtWidgets
from lib.tinydb import TinyDB, Query

db = TinyDB('highscores.json')


def main():
    app = QtWidgets.QApplication([])

    gameMessage = QtWidgets.QLabel('Welcome to Number Guess')


    guess = Guess(gameMessage)
    difficulty = Difficulty(gameMessage)
    previous_guesses = PreviousGuesses()

    highscores = Highscores(db, 'chris', difficulty)
    game = Game(guess, previous_guesses, highscores, difficulty, gameMessage)
    # username_window = UsernameWindow()
    # username_window.show()
    game_window = GameWindow(game, gameMessage)
    game_window.show()
    sys.exit(app.exec_())
    # game.run()

main()
