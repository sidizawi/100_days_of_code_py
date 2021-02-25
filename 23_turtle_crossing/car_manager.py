from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.distance = STARTING_MOVE_DISTANCE
        self.init_cars()
    
    def init_cars(self):
        for i in range(3):
            self.create_car()

    def create_car(self):
        new_car = Turtle()
        new_car.up()
        new_car.color(choice(COLORS))
        new_car.shape("square")
        new_car.setheading(180)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(randint(320, 400), randint(-230, 230))
        self.cars.append(new_car)
    
    def increment(self):
        self.change_pos()
        self.distance += MOVE_INCREMENT

    def change_pos(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.goto(randint(320, 400), randint(-230, 230))

    def move(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.goto(randint(320, 400), randint(-230, 230))
            car.fd(self.distance)
    
    def check_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 15:
                return True
        return False
