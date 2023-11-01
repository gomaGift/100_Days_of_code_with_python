from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-345, 275)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"level {self.level}: ", align="left", font=("Arial", 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=("Arial", 15, 'normal'))

    def clear_game_over(self):
        self.goto(0, 0)
        self.clear()

    def increase_level(self):
        self.level += 1
        self.update_score()
