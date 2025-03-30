from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.speed_value = 0.3

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.turtlesize(stretch_len = 1, stretch_wid = 1, outline = 1)
        self.speed(0)

    def move_ball(self, theta):
        self.penup()
        self.setheading(theta)
        self.fd(self.speed_value)

    def ball_flash(self, screen):
        for i in range(5):
            self.ht()
            screen.update()
            time.sleep(0.1)
            self.st()
            screen.update()
            time.sleep(0.1)
        pass