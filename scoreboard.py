from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.P1_score = 0
        self.P2_score = 0
        self.hideturtle()
        self.pencolor("white")
        self.pensize(5)
        self.speed(0)
        
    def update_score(self):
        self.clear()
        self.penup()
        self.goto(-100, 260)
        self.pendown()
        self.write(arg = f"Player 1: {self.P1_score}", move = False, align = "center", font = ("Arial", 20, "normal"))
        self.penup()
        self.goto(100, 260)
        self.pendown()
        self.write(arg = f"Player 2: {self.P2_score}", move = False, align = "center", font = ("Arial", 20, "normal")) 
        self.penup()