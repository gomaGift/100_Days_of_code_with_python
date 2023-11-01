import time
from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("high-score.txt") as file:
            self.high_score = int(file.read())
        self.indicate_score()

    def increase_score(self):
        self.score += 1
        self.indicate_score()

    def indicate_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}. HighScore: {self.high_score}.", move=False, align="center",
                   font=('Arial', 15, 'normal'))

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high-score.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.indicate_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=('Arial', 15, 'normal'))

