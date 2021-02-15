from turtle import Turtle, Screen
from random import choice
# import colorgram

# colors = colorgram.extract("image.jpg", 30)

# lst = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     lst.append((r, g, b))
# print(lst)

colors = [(247, 239, 243), (131, 165, 206), (225, 151, 100), (32, 41, 59), (200, 134, 147), (235, 212, 87), (166, 56, 46), 
(39, 104, 153), (141, 184, 161), (153, 58, 65), (170, 29, 33), (217, 80, 69), (158, 32, 29), (15, 96, 71), 
(236, 165, 156), (50, 111, 90), (58, 50, 47), (50, 42, 46), (228, 164, 168), (34, 61, 56), (170, 188, 222),
(190, 99, 108), (32, 59, 108), (103, 127, 163), (34, 151, 210), (175, 200, 188), (66, 66, 56)]

bob = Turtle()
bob.speed("fastest")
screen = Screen()
screen.colormode(255)

def go(tub):
    bob.penup()
    bob.goto(tub)
    bob.pendown()

def draw_hirst():
    go((-500, -500))
    for _ in range(20):
        for _ in range(20):
            bob.dot(20, choice(colors))
            go((bob.pos()[0] + 50, bob.pos()[1]))
        go((-500, bob.pos()[1] + 50))

draw_hirst()

screen.exitonclick()
