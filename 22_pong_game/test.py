from turtle import Turtle as t
from turtle import Screen

screen = Screen()
bob = t()
bob.shape("square")
bob.shapesize(stretch_wid=5, stretch_len=1)
screen.exitonclick()