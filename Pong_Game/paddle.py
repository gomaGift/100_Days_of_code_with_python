from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cod):
        super().__init__()
        self.create_paddle(x_cod)

    # creates a paddle
    def create_paddle(self, x_cod):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=3.5)
        self.penup()
        self.setheading(270)
        self.goto(x_cod, 0)

    # maintains the x_cord and moves the paddle up by 20 paces
    def move_up(self):
        if self.ycor() < 320:
            self.goto(self.xcor(), self.ycor() + 20)

    # maintains the y_cord and moves the paddle down by 20 paces
    def move_down(self):
        if self.ycor() > -290:
            self.goto(self.xcor(), self.ycor() - 20)
