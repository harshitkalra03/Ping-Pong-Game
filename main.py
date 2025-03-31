from turtle import Screen
from paddle import Paddle
from ball import Ball
from arena import Arena
from scoreboard import Scoreboard
import time
import random

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 800
CANVAS_COLOR = "black"

GAME_ON = True

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

arena = Arena()
arena.seperator()
arena.create_border()
canvas.update()

scoreboard = Scoreboard()
scoreboard.update_score()

canvas.listen()
canvas.onkeypress(fun = left_paddle.move_up, key = "w")
canvas.onkeypress(fun = left_paddle.move_down, key = "s")
canvas.onkeypress(fun = right_paddle.move_up, key = "Up")
canvas.onkeypress(fun = right_paddle.move_down, key = "Down")

while GAME_ON:
    time.sleep(pong_ball.speed_value)
    canvas.update()
    pong_ball.move_ball()
  
    if pong_ball.ycor() >= 280 or pong_ball.ycor() <= -270:
        pong_ball.bounce_y()
        canvas.update()     

    if (pong_ball.distance(right_paddle)<50 and pong_ball.xcor() > 320) or (pong_ball.distance(left_paddle)<50 and pong_ball.xcor() < -320):
        pong_ball.bounce_x()
        canvas.update()

    if pong_ball.xcor() > 400:
        pong_ball.reset_position()
        pong_ball.ball_flash(screen=canvas)
        scoreboard.l_point()

    if pong_ball.xcor() < -400:
        pong_ball.reset_position()
        pong_ball.ball_flash(screen=canvas)
        scoreboard.r_point()

canvas.exitonclick()    