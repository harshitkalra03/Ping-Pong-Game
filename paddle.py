from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len = 1, stretch_wid = 5, outline = 1)

    def move_to(self, x, y):
        self.penup()
        self.goto(x = x, y = y)

    def move_up(self):
        new_ycor = self.ycor() + 20
        if new_ycor <= 240:
            new_position = (self.xcor(), new_ycor)
            self.goto(new_position)

    def move_down(self):
        new_ycor = self.ycor() - 20
        if new_ycor >= -240:
            new_position = (self.xcor(), self.ycor() - 20)
            self.goto(new_position)