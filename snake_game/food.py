from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.reset()

    def reset(self):
        x_cord = random.randint(-280, 280)
        y_cord = random.randint(-280, 280)
        self.goto(x_cord, y_cord)

