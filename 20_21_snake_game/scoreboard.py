from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		with open("data.txt") as f:
			self.high_score = int(f.readline())
		self.up()
		self.color("white")
		self.goto(0, 270)
		self.update_score()
		self.hideturtle()

	def update_score(self):
		self.clear()
		self.write(f"Score : {self.score} High Score: {self.high_score}", align=ALIGNEMENT, font=FONT)

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			with open("data.txt", 'w') as f:
				f.write(str(self.high_score))
		self.score = 0

	def increase_score(self):
		self.score += 1
		self.update_score()
