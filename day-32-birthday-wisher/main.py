# # 001 Day 32 Goals what we will make by the end of the day
# # 002 A Note About the Next Lesson Google SMTP Port
# # 003 How to Send Emails with Python using SMTP
# import smtplib
#
# my_email = "alintxxipython@gmail.com"  # *xKFQF3iJE:u)2W1k.j,,N10apQhaV
# password = "jnwxzrbemsckbxxu"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="appbrewerytesting@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )


# # 004 Working with the datetime Module
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)


# # 005 Challenge 1 - Send Motivational Quotes on Mondays via Email
# import smtplib
# import datetime as dt
# import random
#
# MY_EMAIL = "alintxxipython@gmail.com"
# MY_PASSWORD = "jnwxzrbemsckbxxu"
#
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 1:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg=f"subject:Monday Motivation\n\n{quote}"
#         )


# # 006 Automated Birthday Wisher Project Challenge
##################### Extra Hard Starting Project ######################
# # 1. Update the birthdays.csv
# # 2. Check if today matches a birthday in the birthdays.csv
# # 3. If step 2 is true,
# # pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# # 4. Send the letter generated in step 3 to that person's email address.

import smtplib
from datetime import datetime
import pandas
import random

MY_EMAIL = "alintxxipython@gmail.com"
MY_PASSWORD = "jnwxzrbemsckbxxu"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"subject:Happy Birthday {birthday_person['name']}\n\n{contents}"
        )

# # 007 Solution & Walkthrough for the Automated Birthday Wisher
# # 008 Run Your Python Code in the Cloud!
# # pythonanywhere.org
