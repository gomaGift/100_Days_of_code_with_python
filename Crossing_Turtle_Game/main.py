import random
import time
from turtle import Turtle, Screen
from turtle_the_crosser import TurtleTheCrosser
from barriers import Barrier
from scoreboard import Scoreboard

NUMBER_OF_BARRIERS = 20

screen = Screen()
screen.setup(width=700, height=600)
screen.tracer(0)
screen.listen()

barriers = []


def create_barrier(listing):
    for j in range(20):
        bar = Barrier()
        listing.append(bar)


create_barrier(barriers)
level_board = Scoreboard()
crosser = TurtleTheCrosser()
screen.onkey(fun=crosser.move_up, key="u")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    # move the barriers
    for i in barriers:
        i.back(i.move_distance)

        # detect if the a barrier reaches the utmost left
        if i.xcor() < -350:
            i.goto(350, random.randint(-255, 265))
        # detect turtle collision with the barrier
        if crosser.distance(i) < 20:
            level_board.game_over()
            time.sleep(1)
            level_board.clear()
            crosser.reset()
            level_board = Scoreboard()
            for barrier in barriers:
                barrier.goto(-1000, 1000)
            barriers.clear()
            create_barrier(barriers)

    # detect if turtle successfully crosses the tar
    if crosser.ycor() > 280:
        crosser.reset()
        level_board.increase_level()
        for i in barriers:
            i.increase_move_distance()

screen.exitonclick()
