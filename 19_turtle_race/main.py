from turtle import Turtle, Screen
from random import randint

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
pos = [150, 90, 30, -30, -90, -150]
all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)

for index in range(0, 6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.color(colours[index])
	new_turtle.up()
	new_turtle.goto(x=-230, y=pos[index])
	all_turtles.append(new_turtle)

user_bet = screen.textinput("Make your bet", "Who will win the race? Enter a colour:")

race_on = False

if user_bet in colours:
	race_on = True
else:
	print("bad input")
	screen.bye()

while race_on:
	for turtle in all_turtles:
		dis = randint(0, 10)
		turtle.fd(dis)
		if turtle.xcor() > 230:
			race_on = False
			win_color = turtle.pencolor()
			if (win_color == user_bet):
				print(f"You've won! The {win_color} turtle is the winner!")
			else:
				print(f"You lose. The {win_color} turtle is the winner!")
			screen.bye()

screen.exitonclick()