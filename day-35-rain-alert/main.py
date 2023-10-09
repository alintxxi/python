# # Day 35 - Intermediate+
# # Keys, Authentication & Environment Variables Send SMS

# # 001 Day 35 Goals what you will make by the end of the day
# # 002 What is API Authentication and Why Do We Need to Authenticate Ourselves
# # 003 Using API Keys to Authenticate and Get the Weather from OpenWeatherMap
import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "a9784565a0531b0079173f475e46151e"

weather_params = {
    "lat": 35.800286309182326,
    "lon": 51.51265090920069,
    "appid": api_key,
}


response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

print(data)
