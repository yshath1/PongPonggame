from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong game")
screen.tracer(0)

tim = Paddle()
tim.move()
scoreboard_left=Score((-150,270))
scoreboard_right=Score((150,270))
ball = Ball()
screen.listen()
screen.onkey(tim.Up, "Up")
screen.onkey(tim.Down, "Down")
screen.onkey(tim.w_key, "w")
screen.onkey(tim.x_key, "x")
game_is_on = True
speed=0.10
while game_is_on:
    if speed < 0.01:
        speed = 0.01
    else:
        time.sleep(speed)
    ball.move()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < - 280:
        screen.update()
        ball.return_back_y()

    if ball.distance(tim.pad[1]) < 50 and ball.xcor() < -320 or ball.distance(tim.pad[0]) < 50 and ball.xcor() > 320:
        ball.return_back_x()


    if  ball.xcor() > 380:
        ball.move_right_pad()
        scoreboard_left.increase_score()
        speed-=0.01



    if   ball.xcor() < -380:
        screen.update()
        ball.move_left_pad()
        scoreboard_right.increase_score()
        speed -= 0.01



screen.exitonclick()
