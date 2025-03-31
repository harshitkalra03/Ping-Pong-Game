from turtle import Turtle

class Arena(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.pensize(5)
        self.speed(0)

    def seperator(self):
        self.penup()
        self.goto(0, 275)
        self.setheading(270)
        for _ in range(14):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)
    
    def create_border(self):
        self.penup()
        self.goto(-385, 290)
        self.pendown()
        self.setheading(0)
        for _ in range(2):
            self.fd(760)
            self.right(90)
            self.fd(570)
            self.right(90)
        self.penup()