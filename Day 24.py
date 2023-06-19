# Day 24
# CONCEPTS 
# # open method
# file = open("text.txt")
# contents = file.read() #Returns the contents of the text file in a string
# print(contents)
# file.close()

# # use forward slash to read the file directory
# # with: we don't have to close the file
# with open("C:/Users/detec/OneDrive/Desktop") as file:
#     contents = file.read()  # Returns the contents of the text file in a string
#     print(contents)

# ## Write mode / w
# with open("text.txt", mode = 'w') as file:
#     file.write("New text.")
#     print(file)

# ## Append a new text
# with open("text.txt", mode = 'a') as file:
#     file.write("\n New text.")
#     print(file)

# # # Write mode for a file name that does not exist: creates a new file by that name
# with open("new_text.txt", mode = 'w') as file:
#     file.write("New text.")


####################### Birthday Letters for friends ################################
# Invited Names.txt
'''
Aang
Zuko
Appa
Katara
Sokka
Momo
Uncle Iroh
Toph
'''

# Starting letter.txt
'''
Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Angela
'''

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Creating a list from the Invited_names
with open("./Input/Names/invited_names.txt") as names_list:
    list_of_names =[]
    for name in names_list:
        list_of_names.append(name.replace("\n",''))

print(list_of_names)

# Creating a variable for name from the starting letter
with open("./Input/Letters/starting_letter.txt") as starting_letters:
    contents = starting_letters.read()

# Saving the file in a new location
for name in list_of_names:
    with open(f"letter_for_{name}", 'w') as file:
        new_text = contents.replace("[name]", name)
        file.write(new_text)
