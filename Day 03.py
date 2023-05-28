'''
Day 03 
Conditional Operators, Logical operators 
'''

#----------------Rollercoaster----------
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollcoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

# #---------Odd or Even ------------------
# # 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#----------Nested if/else statement------
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollcoaster!")
  age= int(input("What is your age? "))
  if age<12:
    print("Please pay $5.")
  elif age <=18:
    print("Please pay $7.")
  elif age >=18 and not(age >= 45 or age <= 55):
    print("Please pay $12.")
  elif age >= 45 or age <= 55:
    print("Please pay $0.") 

else:
  print("Sorry, you have to grow taller before you can ride.")

#----------------BMI 2.0 Exercise----------
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight/ height**2
bmi = round(bmi)
if bmi < 18.5: 
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <25: 
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi<35:
    print(f"Your BMI is {bmi}, you are obese")
else: 
    print(f"Your BMI is {bmi}, you are clinically obese")

#------------Leap Year Exercise-----------
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
if year % 4 != 0:
    print("Not leap year.")
else:
    if year % 100 != 0:
        print("Leap year.")
    else:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")

#-------Pizza Order Practice----------
# # 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
bill = 0 
if size == 'S': 
    bill = 15 
    if add_pepperoni == 'Y':
        bill+= 2 

elif size == 'M':
    bill = 20
    if add_pepperoni == 'Y':
        bill+=3

else:
    bill = 25
    if add_pepperoni == 'Y':
        bill+=3
if extra_cheese == 'Y':
  bill+=1
print(f"Your final bill is: ${bill}.")

# #-------------Love Calculator------------
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1 + name2
lower_combined_string = combined_string.lower()

t = lower_combined_string.count("t")
r = lower_combined_string.count("r")
u = lower_combined_string.count("u")
e = lower_combined_string.count("e")

true = t + r + u + e 

l = lower_combined_string.count("l")
o = lower_combined_string.count("o")
v = lower_combined_string.count("v")
e = lower_combined_string.count("e")

love = l + o + v + e 
lovescore = int(str(true) + str(love))

if (lovescore <10) or (lovescore >90):
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif (lovescore >=40) and (lovescore<= 50):
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}")

#-------- Treasure Island Project --------
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = input('Which way do you wanna go? Left or Right').lower()
if direction == 'left':
    swim_or_wait= input("Swim or Wait?").lower()
    if swim_or_wait == 'wait':
        door = input("Which door do you wish to take? Red, blue, yellow").lower()
        if door == 'yellow':
            print("You Win !")
        else: 
            print("Game Over")
    else: 
        print("Game Over")
elif direction == 'Right' or 'right':
    print("Game Over")
