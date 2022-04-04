from turtle import Turtle

MOVE_DISTANCE = 20
DOWN = 270
UP = 90
STARTING_POSITION = [(350, 0), (-350, 0)]


class Paddle():
    def __init__(self):
        self.pad = []
        self.create_paddle()

    def create_paddle(self):
        for i in STARTING_POSITION:
            new_part = Turtle("square")
            new_part.color("white")
            new_part.shapesize(1, 5)
            new_part.penup()
            new_part.goto(i)
            self.pad.append(new_part)

    def move(self):
        self.pad[1].setheading(UP)
        self.pad[1].forward(100)
        self.pad[0].setheading(UP)
        self.pad[0].forward(100)

    def Up(self):
        self.pad[0].setheading(UP)
        self.pad[0].forward(20)

    def Down(self):
        self.pad[0].backward(20)

    def w_key(self):
        self.pad[1].setheading(UP)
        self.pad[1].forward(20)

    def x_key(self):
        self.pad[1].backward(20)
