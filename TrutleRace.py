from turtle import Turtle, Screen
import random

screen= Screen()
#For the race the screen size is important as the turtle who first reaches the edge of the right screen will win
screen.setup(width=500,height=400)
# Input from the user who would choose a color before the race begins to make their bet.
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
#print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle= Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index]) #creating 6 different colored turtles for the race
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index]) #giving all the turtles a starting point
    all_turtles.append(new_turtle)

if user_bet:
    race_on=True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230: # any turtle reaches the edge of the screen, race should get over
            race_on=False
            winning_color = turtle.pencolor()
            if winning_color==user_bet:
                print(f"You won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost! The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance) 



screen.exitonclick()
