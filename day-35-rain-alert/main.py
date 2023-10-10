# # Day 35 - Intermediate+
# # Keys, Authentication & Environment Variables Send SMS

# # 001 Day 35 Goals what you will make by the end of the day
# # 002 What is API Authentication and Why Do We Need to Authenticate Ourselves
# # 003 Using API Keys to Authenticate and Get the Weather from OpenWeatherMap
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "a9784565a0531b0079173f475e46151e"
account_sid = "AC123c80e05283e5e81a19328190cd0839"
auth_token = "5eabfcf6f564b8c4331985dc3f634b47"

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
    # # 006 Use PythonAnywhere to Automate the Python Script
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    # # 005 Sending SMS via the Twilio API
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_='+12673092068',
        to='+989127374348'
    )

    print(message.status)
