from turtle import Turtle

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