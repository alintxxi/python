from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color win the race? choose a color: ")
colors = ["red", "blue", "cyan", "green", "pink", "brown"]
y_position = [-80, -48, -16, 16, 48, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)





screen.exitonclick()