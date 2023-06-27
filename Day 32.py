# Day 32
# Birthdays Wisher 

# Importing modules
from datetime import datetime
import random
import smtplib
import pandas

# Email and password details
my_email = "newmail.com"
password = "new_password" #for gmail

# Creating a tuple from today's month and day using datetime
today = datetime.now()
today_tuple = (today.month, today.day)

# Use pandas to read our csv file
data = pandas.read_csv('birthdays.csv')

# Create a dictionary from birthday.csv using dictionary comprehension
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in data.iterrows()}

# Compare if today's month/day tuple matches one of the keys in birthdays_dict
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # If true, then pick a random letter from letter template
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        # Replacing [NAME] with the name of the person
        contents = contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday\n\n{contents}")

# birthdays.csv
'''
name,email,year,month,day
test,emailtest,2023,03,23
'''

