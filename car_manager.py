from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.move_in=0

    def create_car(self):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        x = 300
        y = random.randint(-300, 300)
        self.penup()
        self.goto(x, y)

    def car_move(self):
        x=self.xcor()
        y=self.ycor()
        self.goto(x-self.move_in,y)


