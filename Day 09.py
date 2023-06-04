# Day 09: Dictionary, Nesting

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# Retrieving the dictionary value
print(programming_dictionary["Bug"])

# Adding new items to dictionary 
programming_dictionary["Loop"] = "The action of doing something over and ovevr again."
print(programming_dictionary)

#Creating an empty dictionary 
empty_dictionary = {}

#Wipe an existing dictionary 
# programming_dictionary ={}
# print(programming_dictionary)

#Edit an item in a dictionary 
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary 
# only gives the keys 
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

# Grading Program-------------------------------------------------
'''
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.
This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"
'''
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades= {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for keys in student_scores:
    values = student_scores[keys]
    if values in range (91,101):
        student_grades[keys]= "Outstanding"
    elif values in range (81, 91):
        student_grades[keys]="Exceeds Expectations"
    elif values in range (71, 81):
        student_grades[keys]="Acceptable"
    elif values in range (70):
        student_grades[keys]="Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

# Dictionaries 
travel_log= {
  "France":["Paris", "Lille", "Dijon"],
  "Germany":["Berlin", "Hamburg", "Stuttgart"]}

# Nesting Dictionary in a Dictionary
travel_log= {
  "France":{"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany":{"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 10}
}
print(travel_log)

# Nesting Dictionary in a List 
travel_log = [
  {"country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12
  },
  {"country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_vists": 5
  }
]

## Exercise: 
'''
You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
You've visited Russia 2 times.

You've been to Moscow and Saint Petersburg.'''
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
new_entry={}
cities_names=[]
def add_new_country(country_name, total_visits, cities_names):
    new_entry["country"]= country_name
    new_entry["visits"]= total_visits
    new_entry["cities"]= cities_names
    travel_log.append(new_entry)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

### The Secret Auction Program ------------------------------------------------------------------------------
from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''