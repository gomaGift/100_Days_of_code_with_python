import random
from turtle import Turtle, colormode


class Barrier(Turtle):

    def __init__(self):
        super().__init__()
        self.create_barriers()
        self.r = 0
        self.g = 0
        self.b = 0
        self.move_distance = 10

    def create_barriers(self):
        self.shape("square")
        self.color(self.random_color())
        self.shapesize(stretch_wid=1, stretch_len=2.8)
        self.penup()
        y = random.randint(-255, 265)
        self.goto(random.randint(-350, 350), y)

    colormode(255)

    def random_color(self):
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        return self.r, self.g, self.b

    def increase_move_distance(self):
        self.move_distance += 5
