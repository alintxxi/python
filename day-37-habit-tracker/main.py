# # Day 37
# # Intermediate+
# # Habit Tracking Project API Post Requests & Headers

# # 001 Day 37 Goals what you will make by the end of the day
# # 002 HTTP Post Requests
import requests
from datetime import datetime

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

# # POST
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

today = datetime.now()

pixel_data = {
    # # 005 Autofilling today's date using strftime
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)
# # {"message":"Success.","isSuccess":true}

# # 006 How to use HTTP Put and Delete Requests
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "9.1",
}

# # PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)
# # {"message":"Success.","isSuccess":true}

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# # DELETE
# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
# # {"message":"Success.","isSuccess":true}
