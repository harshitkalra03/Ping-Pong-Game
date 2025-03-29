from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import math
import random

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 800
CANVAS_COLOR = "black"

GAME_ON = True

ball_direction = random.randint(0, 360)
canvas = Screen()
canvas.setup(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.bgcolor(CANVAS_COLOR)
canvas.title("Welcome to the PING-PONG Game!")
canvas.tracer(n = 0)

left_paddle = Paddle()
left_paddle.move_to(x = -350, y = 0)

right_paddle = Paddle()
right_paddle.move_to(x = 350, y = 0)

pong_ball = Ball()

canvas.update()

canvas.listen()

canvas.onkeypress(fun = left_paddle.move_up, key = "w")
canvas.onkeypress(fun = left_paddle.move_down, key = "s")
canvas.onkeypress(fun = right_paddle.move_up, key = "Up")
canvas.onkeypress(fun = right_paddle.move_down, key = "Down")

while GAME_ON:
    canvas.update()
    pong_ball.move_ball(theta = ball_direction)
    if pong_ball.ycor() >= 290 or pong_ball.ycor() <= -290:
        ball_direction = math.pi - pong_ball.heading()

    if (pong_ball.xcor() >=340 and pong_ball.xcor() <=350) or (pong_ball.xcor() <= -340 and pong_ball.xcor() >=-350):
        if (pong_ball.ycor() <= right_paddle.ycor() + 50 and pong_ball.ycor() >= right_paddle.ycor() -50) or (pong_ball.ycor() <= left_paddle.ycor() + 50 and pong_ball.ycor() >= left_paddle.ycor() -50):
            ball_direction = math.pi - pong_ball.heading()

canvas.exitonclick()    