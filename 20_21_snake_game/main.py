from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_on = True
while game_on:
	screen.update()
	time.sleep(.1)
	snake.move()

	#collision with food
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		scoreboard.write_score()
	
	#collision with wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		game_on = False
		scoreboard.game_over()

	#collision with tail
	for seg in snake.segments[1:]:
		if snake.head.distance(seg) < 10:
			game_on = False
			scoreboard.game_over()

screen.exitonclick()
