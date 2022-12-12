from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# keyboard control keys
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move_func()
    # detect the snake collision with food
    if snake.head.distance(food) < 15:
        food.reset()
        snake.add_segment()
        scoreboard.increase_score()

    # detect snake collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()

    # detect snake collision with any segment of its tail
    for part in snake.parts[1:]:
        if snake.head.distance(part) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
