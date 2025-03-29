from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.turtlesize(stretch_len = 1, stretch_wid = 1, outline = 1)

    def move_ball(self, theta):
        self.penup()
        self.speed("fastest")
        self.setheading(theta)
        self.fd(0.2)