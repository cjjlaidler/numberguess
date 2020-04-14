class Highscores:

    difficulty_setting = {
        1: 'easy',
        2: 'medium',
        3: 'hard'
    }

    def __init__(self, db, username, difficulty):
        self.db = db
        self.username = username
        self.difficulty = difficulty

    def add_highscore(self, score: int):
        self.db.insert({
            'username': self.username,
            'difficulty': self.difficulty_setting[self.difficulty.value],
            'score': score
        })

    def print_highscores(self):
        print('\nCurrent highscores:\n')
        print(self.db.all(), "\n")
