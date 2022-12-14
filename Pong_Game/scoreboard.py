from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x_cod, y_cod):
        super().__init__()
        self.score = -1
        self.x = x_cod
        self.y = y_cod
        self.display_score()

    # writes the score to the screen
    def display_score(self):
        self.score += 1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(self.x, self.y)
        self.clear()
        self.write(arg=f"{self.score}", align="right", font=("Consolas", 30, "normal"))
