from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = -1
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.speed("fastest")
        self.penup()
        self.goto(0, 270)
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=('Arial', 15, 'normal'))
