from turtle import Turtle

FONT_NAME = "ARIAL"
FONT_SIZE = 20
FONT_TYPE = "normal"
FONT = (FONT_NAME, FONT_SIZE, FONT_TYPE)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.P1_score = 0
        self.P2_score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.speed(0)
        
    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(arg = f"Player 1: {self.P1_score}", move = False, align = "center", font = (FONT))
        self.goto(100, 250)
        self.write(arg = f"Player 2: {self.P2_score}", move = False, align = "center", font = (FONT)) 
    
    def l_point(self):
        self.P1_score += 1
        self.update_score()
    
    def r_point(self):
        self.P2_score += 1
        self.update_score()