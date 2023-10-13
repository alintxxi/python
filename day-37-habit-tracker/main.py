# # Day 37
# # Intermediate+
# # Habit Tracking Project API Post Requests & Headers

# # 001 Day 37 Goals what you will make by the end of the day
# # 002 HTTP Post Requests
import requests

USERNAME = "alintxxi"
TOKEN = "xbRAeQWndLP8nc2k6Kh61"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# # {"message":"Success. Let's visit https://pixe.la/@alintxxi , it is your profile page!","isSuccess":true}

# # 003 Advanced Authentication using an HTTP Header
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# # {"message":"Success.","isSuccess":true}

# # 004 Challenge Add a Pixel to the Habit Tracker using a Post Request
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": "20231013",
    "quantity": "2.1",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)
# # {"message":"Success.","isSuccess":true}
