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
    username_window = UsernameWindow()
    username_window.show()
    game_window = GameWindow(username_window.username)
    game_window.show()
    sys.exit(app.exec_())


    guess = Guess()
    difficulty = Difficulty()
    previous_guesses = PreviousGuesses()

    highscores = Highscores(db, username_window, difficulty)
    game = Game(guess, previous_guesses, highscores, difficulty)
    # game.run()

main()
