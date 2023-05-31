# Day 06 
# Defining Functions and Calling Functions 
def my_function():
  print("Hello")
  print("Bye")

my_function()

'''
Reeborg's World Link 
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
'''
# Control + [ 
# control + ]
def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
def one_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for step in range(6):
    one_jump()

##---------------------While Loops------------------
while something_is_true: 
  #Do something repeatedly 

#Only stops performing when this condition becomes false 
number of hurdles = 6
while number_of_hurdles >0:
  jump()
  number_of_hurdles -=1
  print(number_of_hurdles)

# For loops are great when we iterate over each item in a list
#A while loop can become an infinite loop if the condition will never be false
#example: 
# while 5>3:
# do this task 

while not at_goal():
    if wall_in_front():
        one_jump()
    else:
        move()

## When height of hurdle is unknown 
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def one_jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        one_jump()
    else:
        move()

##------------------- For Random Maze----------------------
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
        while wall_in_front():
            if wall_on_right():
                turn_left()
                if wall_in_front():
                    turn_left()
            elif right_is_clear():
                turn_right()
                move()
        while not wall_in_front():
            if wall_on_right():
                turn_left()
                if wall_in_front():
                    turn_right()
                    move()
                elif right_is_clear():
                    turn_right()
                    move()
                else: 
                    move()
            elif not wall_on_right(): 
                turn_right()
                if not wall_in_front():
                    turn_left()
                    move()


