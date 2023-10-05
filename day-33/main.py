# # Day 33 - Intermediate+ API Endpoints & API Parameters - ISS Overhead Notifier

# # 001 Day 33 Goals what you will make by the end of the day
# # 002 What are Application Programming Interfaces (APIs)

# # 003 API Endpoints and Making API Calls
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
