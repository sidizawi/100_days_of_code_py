from turtle import Turtle

MOVE_DIST = 30

class Paddle(Turtle):

	def __init__(self, start_pos):
		super().__init__()
		self.color("white")
		self.shape("square")
		self.shapesize(stretch_wid=1, stretch_len=5)
		self.up()
		self.goto(start_pos)

	def move(self):
		self.fd(MOVE_DIST)
	
	def go_up(self):
		if self.ycor() < 270:
			self.setheading(90)
			self.move()
	
	def go_down(self):
		if self.ycor() > -270:
			self.setheading(270)
			self.move()
