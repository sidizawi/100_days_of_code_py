from turtle import Turtle
from random import randint, choice

MOVE_DIST = 20

class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.up()
		self.color("white")
		self.shape("circle")
		choices = [randint(-50, 50), randint(-230, -150)]
		start_heading = choice(choices)
		self.setheading(start_heading)
		self.move()
	
	def move(self):
		self.fd(MOVE_DIST)

	def reset(self):
		self.goto(0, 0)
		start_heading = randint(0, 359)
		self.setheading(start_heading)
		self.move()
