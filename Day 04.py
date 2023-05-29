#Day 04 
# Psuedorandom number generator 
import random
# Return a random integer between a and b (inclusive)
random_integer = random.randint(1,10)
print(random_integer)

import my_module
print(my_module.pi)

# Random float numbers- Not include a and b
random_float = random.random()
random_float= random_float*5
print(random_float)

#----------------Coin Toss--------------
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random 
toss = random.randint(0,1)
if toss == 1: 
    print (f"{toss}-'Tails'")
elif toss == 0:
    print(f"{toss}- 'Heads'")
# 0 means Tails and 1 means Heads 

#--------------LISTS------------------
# Positive and negative indexing 
# Append items at end of list 
# Extend a list by another list 

#-------- BANKER ROULETTE--------------
#---Who will pay the bill ------------
# Import the random module here
import random 
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
# splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name
# Write your code below this line 👇
num_items = len(names)
random_choice= random.randint(0, num_items - 1)
person_who_pays = names[random_choice]
print(person_who_pays + " is going to buy the meal today !")

# Another function- choice()
# print(random.choice(list_name))
person_who_pays = random.choice(names)

#------------Position on map--------
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[vertical-1]
selected_row[horizontal-1]='X'
#Write your code above this row 👆

# 🚨 Don't chane the code below 👇
print(f"{row1}\n{row2}\n{row3}")

#Method 2
map[vertical-1][horizontal-1]="X"

#---------Rock Paper Scissors-------------
# Rock wins against scissions 
# Scissors win against paper 
# Paper wins against rock 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. \n"))
if user_choice >=3 or user_choice <0: 
  print("You typed an invalid number, you loose.")
else: 
  print(list[user_choice])
  
  computer_choice = random.randint(0,2)
  print("Computer chose:")
  print(list[computer_choice])

  
  if user_choice == 0 and computer_choice == 2:
    print('You win!')
  elif computer_choice == 2 and user_choice == 2:
    print('You lose!')
  elif user_choice > computer_choice:
    print('You win!')
  elif computer_choice > user_choice: 
    print('You loose')
  elif computer_choice == user_choice: 
    print("It's a draw")





