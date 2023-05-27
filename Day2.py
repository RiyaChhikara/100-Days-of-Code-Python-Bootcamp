print(32342_32424_43432)
# # It ignores underscores in integers (act like commas)

len(21313)
# # object of type 'int' has no len()

num_char = len(input('What is your name? '))
new_num_char = str(num_char)
print("Your name has "+ new_num_char+ " characters.")
# you can only concatenate strings 

# # control+ / to comment out the code 

print (type(num_char))

a = float(123)
print(type(a))

print(70+ float("100.5"))
print(str(70)+str(100))

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
sum = int(two_digit_number[0])+ int(two_digit_number[1])
print(sum)

# PEMDAS 
# Paranthesis, exponent, multiplication, division, add, subtract
print (3*3+3/3-3)

# print(3*(3+3/3-3)) # gives 3 as output 

#---------------------BMI Calculator------------------------
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

Write your code below this line 👇
BMI = int(weight)/ float(height)**2
print(int(BMI))

print(round(8/3,2))
# round upto 2 decimal places 

print(type(8//3))

print(type(4/2))
#It will still be a float type 

result = 4/2
result /=2 #Result will be again divided by 2
print(result)

score = 0 
score = score + 1 
# Can be written as score +=1
# To subtract 1, write score -=1
# To multiply 1, write score *=1
print(score)

num = 100 
num/=10
print(num)

print("your score is "+ str(num))

# f-String
print(f"your score is {score}, your num is {num}")
# All different data types got combined into a string. Use curly braces to include these variables 

# ----------------------------Age Calculator-------------
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)
Rest = 90- age_as_int
days = 365* Rest
weeks = 52* Rest 
months =12* Rest
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# -------------------Tip Calculator---------------------
# If the bill was $150.00, split between 5 people, with 12% tip. 

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# #Write your code below this line 👇
print("Welcome to the tip calculator\n")
total = float(input("What was the total bill? \n $"))
tip = int(input("What percerntage tip would you like to give? 10, 12 or 15?\n"))
split = int(input("How many people to split the bill? "))

tip_as_percent = tip/100 
total_tip = total * tip_as_percent
total_bill = total + total_tip
bill_per_person = total_bill / split
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")

#------------------------------------------

print(max(bool(1), bool(True), bool(10)))











