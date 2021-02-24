from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.up()
		self.color("white")
		self.goto(0, 270)
		self.update_score()
		self.hideturtle()

	def update_score(self):
		self.write(f"Score : {self.score}", align=ALIGNEMENT, font=FONT)

	def game_over(self):
		self.goto(0, 0)
		self.write("Game Over.", align=ALIGNEMENT, font=FONT)

	def write_score(self):
		self.score += 1
		self.clear()
		self.update_score()
