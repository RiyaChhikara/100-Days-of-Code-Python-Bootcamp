# Day 20 
############################################################## Main file 
# Snake game
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
import time

screen = Screen() #Creating an object called sreen from Screen Class
screen.setup(width=600, height=600) # Setting the size of the pop up screen
screen.bgcolor("black")
screen.title("Snake Game") # Naming the screen title
screen.tracer(0) # To prevent the parts moving as disjoint

snake = Snake()

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
screen.exitonclick()

############################################################################# Snake file 
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
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup() # To prevent drawing a line while it moves
            new_segment.goto(position)
            self.segments.append(new_segment)


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
