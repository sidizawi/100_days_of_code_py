from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from middle_line import MiddleLine
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#paddle
left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))

#score
left_score = ScoreBoard("left")
right_score = ScoreBoard("right")

#middle line
MiddleLine()

#ball
game_ball = Ball()

screen.listen()
screen.onkey(key="w", fun=left_paddle.go_up)
screen.onkey(key="s", fun=left_paddle.go_down)
screen.onkey(key="Up", fun=right_paddle.go_up)
screen.onkey(key="Down", fun=right_paddle.go_down)

game_on = True
while game_on:
	screen.update()
	time.sleep(.1)
	game_ball.move()

	#collision with wall
	if game_ball.ycor() >= 280 or game_ball.ycor() <= -280:
		ball_heading = game_ball.heading()
		game_ball.setheading(-ball_heading)
	
	#bounce on paddle
	if left_paddle.distance(game_ball) <= 30 or right_paddle.distance(game_ball) <= 30:
		ball_heading = game_ball.heading()
		game_ball.setheading(180 - ball_heading)

	# if misse paddle
	if game_ball.xcor() > 400:
		game_ball.reset()
		left_score.write_score()
	elif game_ball.xcor() < -400:
		game_ball.reset()
		right_score.write_score()

screen.exitonclick()
