from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.up()
        self.goto(STARTING_POSITION)
    
    def check_pos(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        return False

    def move(self):
        self.fd(MOVE_DISTANCE)
