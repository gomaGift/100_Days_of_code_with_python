from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_distance = 20
        self.y_distance = 20
        self.move_speed = 0.1

    # moves the ball from its current position to another position specified by the x and y distances
    def move(self):
        y = self.ycor() + self.y_distance
        x = self.xcor() + self.x_distance
        self.goto(x, y)

    # repositions the ball at center and changes its x_bounce direction upon collision with the left and right walls
    def reset(self):
        self.goto(0, 0)
        self.x_bounce()
        self.move_speed = 0.1

    # changes the vertical bounce direction upon collision with the vertical walls
    def y_bounce(self):
        self.y_distance *= -1

    # changes the horizontal bounce direction upon collision with the paddles and increases the ball speed
    def x_bounce(self):
        self.x_distance *= -1
        self.move_speed *= 0.95
