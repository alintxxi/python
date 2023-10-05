# # Day 33 - Intermediate+ API Endpoints & API Parameters - ISS Overhead Notifier

# # 001 Day 33 Goals what you will make by the end of the day
# # 002 What are Application Programming Interfaces (APIs)

# # 003 API Endpoints and Making API Calls
# # 004 Working with Responses HTTP Codes, Exceptions & JSON Data
# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()  # Responses HTTP Codes and Exceptions
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

# # 005 Challenge - Build a Kanye Quotes App using the Kanye Rest API
# # 006 Understand API Parameters Match Sunset Times with the Current Time
import requests
from datetime import datetime

MY_LAT = 35.800285
MY_LNG = 51.512684

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)
