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
    "exclude": "current,minutely,daily",
    "appid": api_key,
}


response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# # 004 Challenge - Check if it Will Rain in the Next 12 Hours
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
# print(weather_data["hourly"][0]["weather"][0]["id"])



