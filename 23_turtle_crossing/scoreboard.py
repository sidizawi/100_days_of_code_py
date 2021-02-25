from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.up()
        self.goto(-280, 250)
        self.update_level()
        self.hideturtle()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align="center", font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
