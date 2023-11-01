import random
from turtle import Turtle

MOVE_DIS = 10


class TurtleTheCrosser(Turtle):

    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.reset()

    def move_up(self):
        self.forward(MOVE_DIS)

    def reset(self):
        self.goto(0, -280)
