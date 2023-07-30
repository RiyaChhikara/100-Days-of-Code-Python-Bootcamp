# Day 37
'''
Objective: Advanced Authentication and POST/PUT/DELETE requests
Project: Build a Habit Tracker
Inspiration: Simone Giertz
API used: Pixela #https://docs.pixe.la/
'''

'''
HTTP Requests from requests module 
requests.get()- get piece of data from API provider 
requests.post()- We give some data to the external system . Post a tweet
requests.put()- Update a piece of data. Ex- update a google sheet
requests.delete()- Delete a piece of data like a tweet
'''
import requests
from datetime import datetime

# From datetime module import datetime class

pixela_endpoint = "https://pixe.la/v1/users"

# Constants are usually written in all capital letters.
USERNAME = "
TOKEN = ""
GRAPHID = "graph2023"

# --------------------------- STEP 1----------------------------------------------------------#
# Adding parameters so that we can create a new account (Read API documentation)
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# --------------------------- STEP 2----------------------------------------------------------#
# Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "R programming",
    "unit": "Hours",
    "type": "float",
    "color": "momiji"
}

# keyword arguments or **kw- These are non essential ones, but you can input unlimited keywords
headers = {
    "X-USER-TOKEN": TOKEN
}

# The data that we want to send over
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# --------------------------- STEP 3----------------------------------------------------------#
# Get the graph
# https://pixe.la/v1/users/a-know/graphs/test-graph !
# This is also /v1/users/<username>/graphs/<graphID> API.


# --------------------------- STEP 4----------------------------------------------------------#
# Post value to the graph
# Call /v1/users/<username>/graphs/<graphID> by HTTP POST.

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

# Changing the format of the date using strftime() Method
today = datetime(year=2023, month=7, day=5)
print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),  # yyyymmdd
    "quantity": "2"
}
# response = requests.post(url=pixel_endpoint, json= pixel_data, headers= headers )
# print(response.text)


# --------------------------- STEP 5----------------------------------------------------------#
# Browse again and update values

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

update_data = {
    "quantity": "1"
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers )
# print(response.text)

# Delete a data
response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
