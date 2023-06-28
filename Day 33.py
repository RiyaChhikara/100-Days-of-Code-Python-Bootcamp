# Day 33
# API: Application Programming Interface

'''
Yahoo Weather predictions, Coinbase current market value, NBA stats for players
If we want to use data that they have:

API is a set of commands, functions, protocols and objects that programmers can use
to create software or interact with an external system

Example: Menu is a interface for the user in a restaurant. Contains all the things you can order
You request
They give the response

API Endpoints and API Calls

'''
'''
HTTP Status Codes Glossary

https://www.webfx.com/web-development/glossary/http-status-codes/
1XX: Hold on 
2XX: Here you Go 
3XX: Go Away 
4XX: You Screwed Up 
5XX: I (server) Screwed Up 
'''

# International Space Station location
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# http://api.open-notify.org/iss-now.json

import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
# iss_position = (longitude, latitude)

# print(iss_position)
# https://www.latlong.net/Show-Latitude-Longitude.html

# print(response) # Gives us response code
# if response.status_code == 404:
#     raise Exception('That resource does not exist.')
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data.")
# print(response.status_code)

#https://www.latlong.net/
# Required parameters
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)


########################### KANYE QUOTES PROJECT #############################
from tkinter import *
import requests


def get_quote():
    response = requests.get(url='https://api.kanye.rest/')
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Quote goes here", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()

######################## ISS Overhead ##############################
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

MY_EMAIL = "put_your_mail"
MY_PASSWORD = "mail_password" #for gmail

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <=iss_longitude <=MY_LONG:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <=sunrise:
        return True #It's dark


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg= "Subject:Look Up\n\n The ISS is above you in the sky."
        )




