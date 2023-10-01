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
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)
