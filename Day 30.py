# Day 30
# Errors and Exceptions

'''
Catching Exceptions :

try: Something that might cause an exception
except: Do this if there was an exception
else: Do this if there were no exceptions
finally: Do this no matter what happens
'''

#FileNotFound
# with open("a_file.txt") as file:
#     file.read()
# try:
#     file = open("a_file.txt")
#     a_dictionary ={"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     # There was an error
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message: # Get hold of the error message
#     print(f'That key {error_message} does not exist')
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     raise KeyError("This is an error that I made up.")

# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
# bmi = weight / height ** 2
# print(bmi)

#KeyError
# a_dictionary ={"key": "value"}
# value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Apple"]
# fruit = fruit_list[3]

#TypeError
# text ="abc"
# print(text + 5)

## Exercise-1
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

## Exercise-2
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
print(total_likes)

## 

