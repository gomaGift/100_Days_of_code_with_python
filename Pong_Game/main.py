import time
from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=750, height=700)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

new_seg = Turtle("square")
new_seg.color("white")
new_seg.penup()
new_seg.speed("fastest")
new_seg.hideturtle()
new_seg.goto(0, 350)

new_seg.setheading(270)

# demarcation lines in the middle of the screen
for i in range(22):
    new_seg.pendown()
    new_seg.forward(20)
    new_seg.penup()
    new_seg.forward(20)

scoreboard = Scoreboard(-120, 300)
scoreboard2 = Scoreboard(130, 300)

l_paddle = Paddle(-367)
r_paddle = Paddle(360)
ball = Ball()

# key strokes for detecting paddle movements
screen.onkey(key="u", fun=l_paddle.move_up)
screen.onkey(key="d", fun=l_paddle.move_down)
screen.onkey(key="6", fun=r_paddle.move_up)
screen.onkey(key="8", fun=r_paddle.move_down)


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collisions with the up and down walls
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.y_bounce()

    # detect collisions with the right paddle
    if ball.xcor() < 360 and ball.distance(r_paddle) < 50:
        ball.x_bounce()

    # detect collision with left paddle
    if ball.xcor() > -360 and ball.distance(l_paddle) < 50:
        ball.x_bounce()

    # detect collision with the right wall
    if ball.xcor() > 370:
        ball.reset()
        scoreboard.display_score()

    # detect collision with the left wall
    if ball.xcor() < -370:
        ball.reset()
        scoreboard2.display_score()

screen.exitonclick()
