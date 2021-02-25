from turtle import Turtle

class MiddleLine(Turtle):

	def __init__(self):
		super().__init__()
		self.color("white")
		self.shape("square")
		self.width(5)
		self.draw()
	
	def draw(self):
		self.up()
		self.goto(0, -280)
		self.down()
		self.setheading(90)
		for i in range(56):
			if (self.pen()['pendown']):
				self.up()
			else:
				self.down()
			self.fd(10)
		self.hideturtle()
