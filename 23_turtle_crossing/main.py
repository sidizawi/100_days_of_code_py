import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

gamer = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=gamer.move)

game_is_on = True
loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop += 1

    if loop == 6:
        cars.create_car()
        loop = 0

    # check if turtle finish
    if (gamer.check_pos()):
        cars.increment()
        score.update_level()

    cars.move()

    # check collision
    if cars.check_collision(gamer):
        game_is_on = False
        score.game_over()

screen.exitonclick()