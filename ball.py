import random
from turtle import Turtle


class Ball(Turtle):
    """where the ball is created"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.speed(0)
        self.new_x = 10
        self.new_y = 10
        self.fast=1

    def move(self):
        new_x = self.xcor() + self.new_x
        new_y = self.ycor() + self.new_y
        self.goto(new_x, new_y)

    def return_back_y(self):
        self.new_y *= -1

    def return_back_x(self):
        self.new_x *= -1

    def move_right_pad(self):
        self.goto(0, 0)
        self.new_x *= -1


    def move_left_pad(self):
        self.goto(0, 0)
        self.setheading(45)
        self.new_x = +10
        self.new_y = +10



