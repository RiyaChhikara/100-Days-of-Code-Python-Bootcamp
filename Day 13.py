# # Day 13 
# ############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")

# # This is a bug because 20 will be excluded in the range function
# # we need to change the range to (1,21) from (1,20)
# my_function()

# #Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
# # Here, the dice_nums are more than the dice_imgs indexing. Since, indexing starts from 0, it never reaches 6. 
# # We need to change the randint to (0,5) instead of (1,6)

# # Play Computer
# year = int(input("What's your year of birth?: "))
# if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you? "))
# if age > 18:
#   print(f"You can drive at age {age}.")
# # Bug was indent needed and including f string 

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# # Bug was == (does this variable equal to this value ? This tells true or false)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# # https://pythontutor.com/visualize.html#mode=display

# '''
# Debugging Tips 
# 1. Describe the problem: what am i trying to do ? and what is actually happening ?
# 2. Reproduce the bug if it's an occassional bug
# 3. Act as a computer and evaluate each line (True / False)
# 4. Fixing errors and watch for red underlines 
# 5. Squash bugs with a print() statement: Check values of variables again if they have been updated or not 
# 6. Use a debugger (Thonny or Python Tutor)
# 7. Take a break 
# 8. Ask a friend (developer/ discord)
# 9. Run often (Don't leave it all for the end)
# 10. Stackoverflow
# '''

# # Debugging Exercise 1
# '''
# Syntax error 
# Solution:  Using == instead of = 
# = means assignment 
# == means checking 
# '''
# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# # Debugging Exercise 2
# '''
# TypeError: Not all arguments converted during String formatting 
# Data types 
# type(year) taken as string unless not given as int
# '''
# year =int (input("Which year do you want to check?"))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")
  
# # Debugging Exercise 3 
# '''
# using elif statements to check the number for all the conditions, instead of separate if statements 
# '''
# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)

# # Barcode Generator 
# !pip install python-barcode
# import barcode 
# from barcode import Code128 

# def generate_barcode(data):
#     code = Code128(data)
#     print(code.save("barcode"))
#     print("Barcode generated.")

# data = "1234-5678-9012"
# generate_barcode(data)

################################################################################ Area of geometric shapes calculator 
logo = '''

 █████╗ ██████╗ ███████╗ █████╗                                                        
██╔══██╗██╔══██╗██╔════╝██╔══██╗                                                       
███████║██████╔╝█████╗  ███████║                                                       
██╔══██║██╔══██╗██╔══╝  ██╔══██║                                                       
██║  ██║██║  ██║███████╗██║  ██║                                                       
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                       
                                                                                       
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗     
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝    
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗    
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║    
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    
                                                                                      
'''
# Circle - input(radius)
# cone - input(radius, slant_height)
# Rectangle - input(l,b)
# Triangle - input(base, height)
# Area of square- input(side_length)
# Area of cuboid- (length, width, height)
# Cylinder- input(radius, height)

import math
from replit import clear

def game ():
  print(logo)
  print("You want to calculate the area for which shape ? ")
  print (" '0' for circle, \n '1' for cone,\n '2' for rectangle,\n '3' for Triangle,\n '4' for square,\n '5' for cuboid,\n '6' for cylinder")
  
  def choice_results():
    select_choice = int(input("Enter the choice: "))
    if select_choice == 0:
      print ("You selected a circle.")
      radius = float(input("Enter the radius of the circle: "))
      area = round((math.pi * radius ** 2),3)
      print (f"The area of the circle is {area}")
  
    elif select_choice == 1:
      print ("You selected a cone.")
      radius = float(input("Enter the radius of the cone: "))
      slant_height = float(input("Enter the slant height of the cone: "))
      base_area = math.pi * radius ** 2
      lateral_area = math.pi * radius * slant_height 
      total_area = round((base_area + lateral_area),3)
      print (f"The area of the cone is {total_area}")
  
    elif select_choice == 2:
      print ("You selected a rectangle.")
      length = float(input("Enter the length of the rectangle: "))
      breadth = float(input("Enter the breadth of the rectangle: "))
      total_area = round((length * breadth),3)
      print (f"The area of the cone is {total_area}")
  
    #'3' for Triangle
    elif select_choice ==3:
      print ("You selected a Triangle.")
      base = float(input("Enter the length of the triangle: "))
      height = float(input("Enter the height of the triangle: "))
      area = round((0.5 * base * height), 3)
      print (f"The total area of the triangle is {area}")
  
    #'4' for square
    elif select_choice == 4:
      print ("You selected a square.")
      side_length = float(input("Enter the length of square's side: "))
      area = round((side_length **2), 3)
      print(f"The area of the square is {area}")
  
    #'5' for cuboid
    elif select_choice == 5:
      print ("You selected a cuboid.")
      length = float(input("Enter the length of the cuboid: "))
      width = float(input("Enter the width of the cuboid: "))
      height = float(input("Enter the height of the cuboid: "))
      total_area = 2 * (length *width + length *height + width * height)
      total_area = round(total_area, 3)
      print (f"The area of the cuboid is {total_area}")
      
    #'6' for cylinder
    elif select_choice == 6:
      print ("You selected a cylinder.")
      radius = float(input("Enter the radius of the cylinder: "))
      height = float(input("Enter the height of the cylinder: "))
      base_area = math.pi * radius ** 2
      lateral_area = 2 * math.pi * radius * height 
      total_area = round((2 * base_area + lateral_area), 3)
      print (f"The area of the cylinder is {total_area}")
  
    else: 
        if select_choice not in [1,2,3,4,5,6]:
          print ("Make a valid selection. We'll be coming up with more options soon.")
          choice_results()
        else: 
          choice_results()
        
  choice_results()
  
  def start_again():
    if input ("Calculate for a new shape? Type 'y' or 'n': ").lower()== 'y':
      clear()
      game()
    else: 
      clear()
      start_again()
      
  start_again()
  
game()