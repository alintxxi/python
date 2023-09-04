from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-60, -36, -12, 12, 36, 60]



for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_pos[turtle_index])


screen.exitonclick()
