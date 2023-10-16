# # Day 38
# # Intermediate+
# # Workout Tracking Using Google Sheets

# # 001 Day 38 Goals what you will make by the end of the day
import requests
from datetime import datetime

# # 002 Step 1 - Setup API Credentials and Google Spreadsheet
GENDER = "Male"
WEIGHT_KG = 68
HEIGHT_CM = 180
AGE = 36

APP_ID = "960d287e"
API_KEY = "aeab12446674a813729513acd7b32842"

# # 003 Step 2 - Get Exercise Stats with Natural Language Queries
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# # 004 Step 3 - Setup Your Google Sheet with Sheety
# # 005 Step 4 - Saving Data into Google Sheets
sheet_endpoint = "https://api.sheety.co/c5b12b0d32f64a9250892842f01ce886/myWorkouts/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_input)

    print(sheet_response.text)

