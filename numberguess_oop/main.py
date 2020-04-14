from Models.Game import Game
from Models.Guess import Guess
from Models.PreviousGuesses import PreviousGuesses
from Models.Highscores import Highscores
from Models.Difficulty import Difficulty
from lib.tinydb import TinyDB, Query
db = TinyDB('highscores.json')

def main():
    print("\n--- Welcome to Guess the Number ---\n")
    guess = Guess()
    difficulty = Difficulty()
    previousGuesses = PreviousGuesses()
    username = input("What is your username? ")
    highscores = Highscores(db, username, difficulty)
    game = Game(guess, previousGuesses, highscores, difficulty)
    game.run()
main()