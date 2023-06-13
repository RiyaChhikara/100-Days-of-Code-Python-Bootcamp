# Day 19

# # Higher order Function:
# # Passing a function into another function
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1,n2):
#     return n1 - n2
#
# def calculator(n1, n2, func): # Higher Order Function
#     return func(n1,n2)
#
# result = calculator(2,3,add)
# print(result)

# Object State and Instances
# Timmy and Tommy are two turtles are two instances from same Object
# Each Object can have different attributes like colour. They are called State.

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt ="Who will win the race? Enter a colour: " )
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()> 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            print(turtle.color())

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()



# Binding a function to the onkey method
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def counter_clockwise():
    tim.left(10)
def clockwise():
    tim.right(10)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
# Event listeners: listen to clicks or key presses by the user
screen.listen()
screen.onkey(key = "w", fun= move_forward)
screen.onkey(key = "s", fun= move_backward)
screen.onkey(key = "a", fun= counter_clockwise)
screen.onkey(key = "d", fun= clockwise)
screen.onkey(key = "c", fun= clear_drawing)
#When we bind the function as an argument, we do not use the paranthesis, ()
