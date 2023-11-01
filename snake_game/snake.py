import time
import turtle as t

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.parts = []
        for i in STARTING_POSITION:
            part = t.Turtle("square")
            part.color("white")
            part.penup()
            part.goto(i)
            self.sleep = 2
            self.parts.append(part)
        self.head = self.parts[0]
        self.head.color("green")

    def move_func(self):
        time.sleep(self.sleep)
        for i in range(len(self.parts) - 1, 0, -1):
            x_cod = self.parts[i - 1].xcor()
            y_cod = self.parts[i - 1].ycor()
            self.parts[i].goto(x_cod, y_cod)
        self.head.forward(MOVE_DISTANCE)
        self.sleep = 0

    # screen control functions
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def add_segment(self):
        part = t.Turtle("square")
        part.color("white")
        part.penup()
        # take the newly created segment to the current position of the last segment of the snake
        part.goto(self.parts[-1].pos())
        self.parts.append(part)

    def reset_snake(self):
        for seg in self.parts:
            seg.goto(-1000, 1000)
        self.parts.clear()
        self.__init__()
