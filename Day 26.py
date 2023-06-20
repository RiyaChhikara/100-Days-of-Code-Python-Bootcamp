# Day 26
# List Comprehension
'''
List Comprehension: Create a new list from a previous list
new_list = [new_list for item in list]
numbers = [1,2,3]
'''
#### Using for loop
new_list =[]
for n in list:
    n = n+1
new_list.append(add_1)

#### Using List comprehension
# We loop through each of the n in numbers list, and each of the n, we add 1 to it.
new_list = [n+1 for n in numbers]

# List comprehension for letters
name = 'Riya'
new_list = [letter for letter in name]

# Now, the new_list is: ['R', 'i', 'y', 'a']
# Using range
new_list = [num*2 for num in range(1,5)]

# Conditional List Comprehension
new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Dave", "Freddie", "Caroline"]
short_names = [name for name in names if len(name)<=4]

# Conversions through List Comprehension
long_names = [name.upper() for name in names if len(name)>=5 ]

# Exercise 1: Squared Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:
squared_numbers =[number**2 for number in numbers]
#Write your code 👆 above:

print(squared_numbers)

# Exercise 2: Filtering Even Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:
result = [num for num in numbers if (num % 2 ==0)]
#Write your code 👆 above:

print(result)

# Exercise 3: Check for Data overlap
with open("file1.txt") as file1:
    contents_1 = file1.readlines()

with open("file2.txt") as file2:
    contents_2 = file2.readlines()

result = [int(num) for num in contents_1 if num in contents_2]
# Write your code above 👆
print(result)

##### Dictionary Comprehension
new_dict ={new_key:new_value for item in list}
new_dict ={new_key:new_value for (key,value) in dict.items()}
new_dict ={new_key:new_value for (key,value) in dict.items() if test}

import random
names=['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
students_scores = {student:random.randint(1,100) for student in names}

passed_students ={student:score for (student, score)
                  in students_scores.items()
                  if score>= 60}

### Exercise 4: Dictionary Comprehension
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
result = {word:len(word) for word in sentence.split()}
print(result)

#### Exercise 5: Dictionary Comprehension 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {days:temp_c* 9/5 +32 for days,temp_c in weather_c.items()}
print(weather_f)


# Looping through dictionary
for (key,value) in student_dict.items():
    print(value)

### Iterating over a Pandas DataFrame
student_dict ={
    "student": ["Angela", "James", "Lilly"],
    "score": [56,54,43]
}

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through data frame
for (key,value) in student_data_frame.items():
    print(value)

# Loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    print(index)

for (index, row) in student_data_frame.iterrows():
    print(row.student)

for (index, row) in student_data_frame.iterrows():
    print(row.student)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

{new_key:new_value for (index,row) in df.iterrows()}

########################################### NATO_PHONETIC_ALPHABET PROJECT________________
import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter the name: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

'''
letter,code
A,Alfa
B,Bravo
C,Charlie
D,Delta
E,Echo
F,Foxtrot
G,Golf
H,Hotel
I,India
J,Juliet
K,Kilo
L,Lima
M,Mike
N,November
O,Oscar
P,Papa
Q,Quebec
R,Romeo
S,Sierra
T,Tango
U,Uniform
V,Victor
W,Whiskey
X,X-ray
Y,Yankee
Z,Zulu
'''
