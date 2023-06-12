# Day 18
from turtle import Turtle, Screen
import turtle as t
import random

# We create a new Turtle object called timmy_the_turtle
tim = Turtle()

tim.shape("circle")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    new_colour = (r, g, b)
    return new_colour


# timmy_the_turtle.color("purple")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# Tk (tkinter) recognises many symbolic color names, helps in creating graphic user interface

# Draw a square
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# We changed the name by refactoring

# alias name: import turtle as t
# This package has been included in the standard python library


# how to install package in pycharm
import heroes
print(heroes.gen())

# Draw a dashed line: Method 1
# for _ in range(20):
#     tim.forward(10)
#     tim.dot(10, "white")
#     tim.forward(10)

# Draw a dashed line: Method 2
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# 360/ 4 = 90
# 360/ 5 = 72
# random color

# each side 100
# import random
# colours = ["Turquoise", "black", "yellow", "pink", "red", "DarkOliveGreen", "Maroon", "DarkOrchid", "LightPink", "Goldenrod"]
# def loop(times):
#     for x in range(times):
#      tim.forward(100)
#      tim.right(360/times)
#
# for i in range(3,11):
#     tim.color(random.choice(colours))
#     loop(i)

# Draw a random walk
# directions = [0, 90, 190, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for x in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# Draw spirograph
# tim.speed("fastest")
# def draw_spirograph(size_of_gap):
#     for x in range(int(360/ size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading()+ size_of_gap)
# draw_spirograph(5)

# How to generate random colours in r,g,b

# for x in range(3, 11):
#     for x:
#         tim.forward(100)
#         tim.right(360/x)
#         tim.forward(100)
#         tim.right(360/x)
#         tim.forward(100)
#         tim.right(360/3)
#         tim.forward(100)


# tim.forward(100)
# tim.right(360/3)
# tim.forward(100)
# tim.right(360/3)
# tim.forward(100)
# tim.right(360/3)
#
# tim.forward(100)
# tim.right(360/4)
# tim.forward(100)
# tim.right(360/4)
# tim.forward(100)
# tim.right(360/4)
# tim.forward(100)
# tim.right(360/4)
# tim.forward(100)

############## Hirst spot painting
# import colorgram
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
#
# rgb_colors = []
# colors = colorgram.extract('Hirst_painting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
# rgb = first_color.rgb # e.g. (255, 151, 210)
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s

# The colour list extracted from the image by using the colorgram package
color_list = [(252, 245, 248), (218, 154, 108), (132, 171, 195), (221, 73, 89), (213, 132, 150), (26, 119, 151), (240, 208, 99), (122, 176, 149), (39, 120, 84), (20, 164, 203), (139, 87, 63), (219, 84, 77), (133, 81, 99), (174, 185, 216), (23, 167, 124), (236, 160, 173), (161, 209, 169), (5, 95, 115), (170, 153, 78), (236, 168, 155), (54, 59, 93), (151, 208, 222), (35, 61, 79), (95, 127, 177), (36, 86, 57), (233, 213, 16), (72, 75, 48)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


#So that the window stays here:
screen = Screen()
screen.exitonclick()
