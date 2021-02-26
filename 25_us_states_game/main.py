import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
screen.setup(800, 600)
turtle.up()
turtle.hideturtle()

states = pd.read_csv("50_states.csv")

def answer_in_data(answer):
	if answer in states.state.to_list():
		return answer
	return ""


loop = 0
game_on = True
guessed = []
while game_on and loop < 50:
	title = "Guess the State"
	prompt = "What's another state's name?"
	if loop > 0:
		title = f"{loop}/50 States Correct"
	answer = screen.textinput(title=title, prompt=prompt).title()

	if not answer:
		game_on = False
		missing = [state for state in states.state if state not in guessed]
		df = pd.DataFrame({"missing states" : missing})
		df.to_csv("state_to_learn.csv")
	elif answer_in_data(answer):
		loop += 1
		guessed.append(answer)
		x = int(states[states.state == answer].x)
		y = int(states[states.state == answer].y)
		turtle.goto(x, y)
		turtle.write(answer, font=("Arial", 8, "normal"))

