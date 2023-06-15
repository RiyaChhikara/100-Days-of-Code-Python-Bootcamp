# Day 21 
# Snake game 
########################### main.py ####################
'''
1. Create a Snake body - 3 squares
2. How to move the snake
3. Control the snake
4. detect collision with food so that new food generates randomly
5. Create a scoreboard that is automatically updated
6. Detect collision with wall - end game
7. Detect collision with tail - end game
'''

from turtle import Screen
from snake import Snake
from food import Food
from Scoreboard import ScoreBoard
import time

screen = Screen()
# Creating an object called sreen from Screen Class
screen.setup(width=600, height=600) # Setting the size of the pop up screen
screen.bgcolor("black")
screen.title("Snake Game") # Naming the screen title
screen.tracer(0) # To prevent the parts moving as disjoint

# Creating objects from the classes
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# We want this to happen continuously: move the segments
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # Sleep for 0.1 second
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        # If the snake head is within 15 pixels of the food, detect collision
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
    # We have sliced the list so that if segment == snake.head, it shall pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()

################# Scoreboard.py #####################
from turtle import Turtle
#Constants
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0,0) # centre positioning
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
        
########################### snake.py ####################################
from turtle import Turtle

# This is a list with positions as tuples, representing x and y coordinates
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE =20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
# A constant is written in all capital letters

class Snake:

    def __init__(self):
        # Creating a list called segment and appending it with new_segments
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()  # To prevent drawing a line while it moves
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position()) #To get hold of last segment's position


    def move(self):
        #start= len(segments)-1, stop= 0, step= -1 (Reverse Order)
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Binding a function to the onkey method
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
         
######################### food.py ######################################
from turtle import Turtle
import random

class Food(Turtle):
    '''
    How to render itself as a small circle on the screen.
    When snake touches the screen, it's going to move to a new random location
    We want to inherit from the Superclass: Turtle class
    '''
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # 10 * 10 pixels circle will be drawn from this
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        # Because our screen is 600 in height and 600 in width.
        self.goto(random_x, random_y)

###################################### Concept understanding: Class Inhertitance #############################################
# Example 
# '''
# Inherting behaviour and attributes from an existing class 
# Take the methods from a Class and edit more to it. 
# '''
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2

#     def breathe(self):
#          print("Inhale, Exhale.")

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#         # In this example, super class refers to Animal class

#     def breathe(self):
#         super().breathe() #Inheriting the function from super class
#         print("doing this underwater") #Editing the function 

#     def swim(self):
#         print("moving in water.")

# nemo = Fish()
# nemo.breathe()
