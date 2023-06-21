# Day 27
# Mile to Km Converter Project

from tkinter import *
def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609)
    show_cal.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=40, pady=40)

input = Entry(width=7)
input.grid(row=0, column=1)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_equal= Label(text="is equal to")
label_equal.grid(row=1, column=0)

show_cal= Label(text ="0")
show_cal.grid(row=1, column=1)

label_km= Label(text="Km")
label_km.grid(row=1, column=2)

#Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(row=3, column= 1)

window.mainloop()

############################## CONCEPTS ###########################
# Keyword Arguments
def my_function(a, b, c):
    a + b + c
    # Do this with a
    # Then do this with b
    # Finally do this with c


# Advanced Python Arguments
def my_function_defined(a=1, b=2, c=3):
    a + b + c
    # Do this with function
# Function need a required arg,
# but those that are already defined, are not compulsory

# What is the output of this code?
def foo(a, b=4, c=6):
    print(a, b, c)

foo(4, 9)  # Only c get's a default value. The output becomes: 4,9,6


# What is the output of this code?
def foo(a, b=4, c=6):
    print(a, b, c)
foo(1, 7, 9)
# No default values are used. The output becomes: 1,7,9


# What is the output of the code?
def foo(a, b=4, c=6):
    print(a, b, c)
foo(20, c=6)
# It skips over the argument with a default. The output becomes: 20,4,6


# From limited arguments to Unlimited Arguments
def add(n1, n2):
    return n1 + n2


def add(*args):  # *args means this function can accept any number of arguments
    for n in args:
        print(n)


def add(*args):
    for n in args:
        return sum(n)
        print(sum)


# Unlimited Positional Arguments
def add(*args):
    sum =0
    for n in args:
        sum +=n
    return sum

print(add(1,2,3,4,234,23,23,23,256,56,57,75))

def add(*args):
    print(args[0])

# **kwargs: Many Keyworded Arguments
def demo(**kwargs):
    print(kwargs)
    print(type(kwargs)) # Is a dictionary
    print(kwargs["add"]) # Find the key
    for key, value in kwargs.items():
        print(key)
        print(value)

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3,multiply=5) # (2+3) * 5 gives the output: 25

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.colour = kw.get("colour")
        #It won't give an error to the user if he does not mention the colour.
        self.seats = kw.get("seats")

my_car = Car(make = "Nissan", model="GT-R")
print(my_car.model)
print(my_car.colour)  # Gives output:None


# Question:
def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)
# 4 is passed by position.
# 7,3,0 are collected into a tuple.
# x and y are in a keyword dictionary
# Output: 4 (7,3,0) {'x':10, 'y':64}

### CONCEPTS FOR TKINTER ######
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()


# USE EITHER OF THESE METHODS TO CHANGE THE ARG
# my_label["text"]= "New Text"
# my_label.config(text="New Text")


# Layout Position Managers
# pack- Difficult to mention a precise position
# place- Best when we have limited number of widgets
# grid

# Graphic User Interface with Tkinter and Advanced Functions
'''
Silicon Vallwy History:
Movie- Pirates of Silicon Valley
GUI: In 1990s, we had MS-DOS. Allows user to point and click on screen.
Mac Lisa was one of the first that allowed GUI to interact with the computer
Windows was Microsoft's version of GUI
Xerox PARC: the real inventor: LAN, OOP, GUI, mouse
'''
from tkinter import *

# Creating a new window, equivalent to a screen in Turtle library
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=200)

# Create components inside the window

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold", "italic"))
# my_label.pack()  # A geometry management mechanism to pack the label on the window
my_label.grid(column=0, row=0)
my_label.config(padx=100,pady=200)


#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text= new_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=2)

button_2 = Button(text="New Button", command=button_clicked)
button_2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()
# This means:
# while True:listening to what the user is doing to interact with the screen. Has to be at end of program

