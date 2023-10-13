# # Day 37
# # Intermediate+
# # Habit Tracking Project API Post Requests & Headers

# # 001 Day 37 Goals what you will make by the end of the day
# # 002 HTTP Post Requests
import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "xbRAeQWndLP8nc2k6Kh61",
    "username": "alintxxi",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# # {"message":"Success. Let's visit https://pixe.la/@alintxxi , it is your profile page!","isSuccess":true}
