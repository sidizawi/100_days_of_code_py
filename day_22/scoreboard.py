from turtle import Turtle

ALIGNEMENT = "center"
LEFT_POS = (50, 250)
RIGHT_POS = (-50, 250)
FONT = ("Courier", 30, "normal")

class ScoreBoard(Turtle):

	def __init__(self, side):
		super().__init__()
		self.score = 0
		self.up()
		self.color("white")
		if side == "left":
			self.goto(LEFT_POS)
		else:
			self.goto(RIGHT_POS)
		self.update_score()
		self.hideturtle()

	def update_score(self):
		self.write(f"{self.score}", align=ALIGNEMENT, font=FONT)

	def game_over(self):
		self.goto(0, 0)
		self.write("Game Over.", align=ALIGNEMENT, font=FONT)

	def write_score(self):
		self.score += 1
		self.clear()
		self.update_score()
