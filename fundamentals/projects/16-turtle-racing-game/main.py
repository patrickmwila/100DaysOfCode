from turtle import Turtle, Screen
from random import randint


tim_screen = Screen()
tim_screen.title("Turtle Racing Game")
tim_screen.setup(width=500, height=400)
user_bet = tim_screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")

is_race_on = False
colors = ["red", "green", "blue", "yellow", "purple", "chocolate"]
turtles = []
# create a Turtle() object
y_pos = -150
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()

    new_turtle.goto(-230, y_pos)
    y_pos += 60

    turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner!")

        turtle_distance = randint(0, 10)
        turtle.forward(turtle_distance)

tim_screen.exitonclick()  # make sure the screen exits on clik
