FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=0

    def increment_score(self):
        self.clear()
        self.score+=1
        self.update()

    def update(self):
        self.penup()
        self.goto(-280,250)
        self.write(f"Score: {self.score}", align="left", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)