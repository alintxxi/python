from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0) #Turn off animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update() #Because we used tracer
    ball.move()

screen.exitonclick()