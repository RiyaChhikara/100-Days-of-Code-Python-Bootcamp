#Day 12
################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# enemies inside function: 2
# enemies outside function: 1

# Namespaces: giving names to a function/ variable etc
# Local Scope: only valid within the walls of a function 
# Global Scope: available within and outside the function 

## Modifying Global Variable 
enemies =1 
def increase_enemies():
  global enemies 
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
  
# Global Constants 
# These won't be changed unlike variables, so we write in upper case 
PI = 3.14159
URL = "wwww.google.com"
TWITTER_HANDLE = "@riyachhikaraa"


#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
logo = '''


.██████..██....██.███████.███████.███████.....████████.██...██.███████.....
██.......██....██.██......██......██.............██....██...██.██..........
██...███.██....██.█████...███████.███████........██....███████.█████.......
██....██.██....██.██...........██......██........██....██...██.██..........
.██████...██████..███████.███████.███████........██....██...██.███████.....
...........................................................................
...........................................................................
███....██.██....██.███....███.██████..███████.██████......██████...........
████...██.██....██.████..████.██...██.██......██...██..........██..........
██.██..██.██....██.██.████.██.██████..█████...██████........▄███...........
██..██.██.██....██.██..██..██.██...██.██......██...██.......▀▀.............
██...████..██████..██......██.██████..███████.██...██.......██.............
...........................................................................
...........................................................................


'''
from random import randint 
#Set Global constants
EASY_LEVEL_TURNS = 10 
HARD_LEVEL_TURNS = 5
# Tasks to do 

# Function to check answer 
def check_if_correct(user_answer, correct_answer, attempts):
  '''
  Checks user_answer against correct_answer.
  Returns the number of attempts remaining 
  '''
  if user_answer < correct_answer: 
    print ("Too low. Guess again")
    return attempts -1 
  elif user_answer > correct_answer: 
    print ("Too high. Guess again.")
    return attempts -1 
  elif user_answer == correct_answer:
    print (f"You've got it! The answer was {correct_answer}")

# Make function to set difficult 
def set_difficulty():
  level = input("Choose difficulty level. Easy or Difficult: ").lower()
  if level == "easy":
    return EASY_LEVEL_TURNS
  elif level == 'difficult':
    return HARD_LEVEL_TURNS

def game():
  
  # Choosing a random number between 1 and 100 
  print(logo)
  print("Welcome to the Number Guessing Game!! ")
  print("I'm thinking of a number between 1 and 100")
  correct_answer = randint(1,100) #includes 1 and 100 
  print(f"pssst,the correct answer is {correct_answer}")
  
  attempts = set_difficulty()

  # Repeat the functionality if they get it wrong
  user_answer = 0
  while user_answer != correct_answer:
    print(f"You have {attempts} attempts remaining to guess the number.")

    # Let users guess a number   
    user_answer = int(input("Choose a number: "))
    
  # Track number of turns and reduce by 1 if they get it wrong
    attempts = check_if_correct(user_answer, correct_answer, attempts)
    if attempts == 0:
      print(f"You've exhausted all attempts.The answer was {correct_answer}")
      return # Here, we exit the function 
  
game()


