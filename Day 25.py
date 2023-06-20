# Day 25 
######################## U.S Map Guess Game ###############################
# Turtle package only works with .gif format image files

import turtle
import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Check if the guess is among the 50 states
data = pd.read_csv("50_states.csv")
all_states = data['state'].to_list()
guessed_states =[]

while len(guessed_states) <50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states=[]
        for item in all_states:
            if item not in guessed_states:
                missing_states.append(item)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


# def get_mouse_click_coor(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

# csv file
'''
state,x,y
Alabama,139,-77
Alaska,-204,-170
Arizona,-203,-40
Arkansas,57,-53
California,-297,13
Colorado,-112,20
Connecticut,297,96
Delaware,275,42
Florida,220,-145
Georgia,182,-75
Hawaii,-317,-143
Idaho,-216,122
Illinois,95,37
Indiana,133,39
Iowa,38,65
Kansas,-17,5
Kentucky,149,1
Louisiana,59,-114
Maine,319,164
Maryland,288,27
Massachusetts,312,112
Michigan,148,101
Minnesota,23,135
Mississippi,94,-78
Missouri,49,6
Montana,-141,150
Nebraska,-61,66
Nevada,-257,56
New Hampshire,302,127
New Jersey,282,65
New Mexico,-128,-43
New York,236,104
North Carolina,239,-22
North Dakota,-44,158
Ohio,176,52
Oklahoma,-8,-41
Oregon,-278,138
Pennsylvania,238,72
Rhode Island,318,94
South Carolina,218,-51
South Dakota,-44,109
Tennessee,131,-34
Texas,-38,-106
Utah,-189,34
Vermont,282,154
Virginia,234,12
Washington,-257,193
West Virginia,200,20
Wisconsin,83,113
Wyoming,-134,90

'''


########################## PRACTICE CONCEPTS ################################
# Working with comma separated value / CSV
# import pandas
# import pandas as pd

# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)
#
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures  = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# data = pd.read_csv("weather_data.csv")
# # print(data["temp"])
# #
# # data_dict = data.to_dict()
# # print(data_dict)
#
# # temp_list = data["temp"].to_list()
# # total = sum(temp_list)
# # num = len(temp_list)
# # Average = total / num
# # print(round(Average,3))
# #
# # # Get the maximum value out of the data series
# # print(data["temp"].max())
#
# # Get data in row
# data[data.temp == data.temp.max()]
# # This will extract the row entry where in the temperature column, the temperature is maximum
#
# monday = data[data.day == "Monday"]
# print(monday.temp)
# # Converting temperature to Fahrenheit
# converted_temp = monday.temp* 9/5 + 32
# print(converted_temp)

## SQUIRREL CENSUS
# sq_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Gray = sq_data["Primary Fur Color"][sq_data["Primary Fur Color"] == "Gray"].count()
# Cinnamon = sq_data["Primary Fur Color"][sq_data["Primary Fur Color"] == "Cinnamon"].count()
# Black = sq_data["Primary Fur Color"][sq_data["Primary Fur Color"] == "Black"].count()
# #OR
# Grey = len(sq_data[sq_data["Primary Fur Color"] == "Gray"])
# print(Gray)
# print(Cinnamon)
# print(Black)

# data_dict = {
#     "Fur Color": ["Gray", "Red", "Black"],
#     "Count": [Gray, Cinnamon, Black]
# }
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
