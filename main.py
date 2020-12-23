import time
from turtle import Screen
from player import Player
import random
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
all_cars=[]
player=Player()
score=Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")
move_in_car=10

game_is_on = True
while game_is_on:
    random_chance = random.randint(1,6);
    if (random_chance==1):
        car = CarManager()
        car.create_car()
        all_cars.append(car)
    for car_moment in all_cars:
        car_moment.move_in=move_in_car
        car_moment.car_move()
    y=player.ycor()
    x=player.xcor()
    if (y>=280):
        y=-280
        #score.increment_score()
        move_in_car+=5
        for car_moment in all_cars:
            car_moment.move_in=move_in_car;
        player.goto(x,y)
        score.increment_score()
        #print(move_in_car)
    for car_moment in all_cars:
        if car_moment.distance(player)<20:
            game_is_on=False
            break
    time.sleep(0.1)
    score.update()
    screen.update()

score.game_over()
screen.exitonclick()