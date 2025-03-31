from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.speed_value = 0.09
        self.x_move = 10
        self.y_move = 10
        self.penup()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.turtlesize(stretch_len = 1, stretch_wid = 1, outline = 1)
        self.speed(0)

    def move_ball(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed_value *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1
        self.speed_value = 0.09

    def ball_flash(self, screen):
        for i in range(5):
            self.hideturtle()
            time.sleep(0.1)
            screen.update()
            self.showturtle()
            time.sleep(0.1)
            screen.update()