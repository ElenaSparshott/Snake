from re import A
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)      
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over: {self.score}", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        


