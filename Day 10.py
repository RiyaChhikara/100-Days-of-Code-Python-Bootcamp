# Day 10 

## Functions with Outputs------------------
def format_name(f_name, l_name):
  f_name= f_name.title()
  l_name= l_name.title()
  return f_name + " "+ l_name
print(format_name("riya", "chhikara"))

## Multiple Return Values------------------
def format_name(f_name, l_name):
  if f_name=="" or l_name =="":
    return "You didn't provide valid inputs."
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "),
                 input("What is your last name? ")))

## Number of days in a leap and non leap year------------
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(input_year, input_month):
    if input_month > 12 or input_month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    while is_leap(input_year) and input_month == 2:
      return 29
    return month_days[input_month -1]

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

#------------------------------------------------------------------
## Project: Calculator Program: combining dictionaries and Functions 
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

from replit import clear
def add(n1,n2):
  return n1 + n2 

#Subtract 
def subtract(n1, n2):
  return n1 - n2

#Multiply 
def multiply(n1, n2):
  return n1 * n2 

#Divide
def divide(n1, n2):
  return n1/n2 

operations = {"+" : add,
            "-" : subtract, 
           "*" : multiply, 
           "/" : divide}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
    
  for symbol in operations: 
    print(symbol)
  should_continue = True
  
  while should_continue: 
    input_operations = str(input("Pick an operation: "))
    num2 = float(input("What's the next number?: "))
    selected_func = operations[input_operations]
    answer = selected_func(num1, num2)
  
    print (f"{num1} {input_operations} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")== "y":
      num1 = answer
    else: 
      should_continue = False 
      clear()
      calculator()    
      # Recursion: calling a function within the function 
calculator()





