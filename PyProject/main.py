from turtle import Screen, Turtle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("P⚪NG")
screen.tracer(0)


paddle = Turtle()
paddle.shape("square")
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)

def up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(),new_y)

def down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(),new_y)

screen.listen()
screen.onkey(up,"Up")
screen.onkey(down,"Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()