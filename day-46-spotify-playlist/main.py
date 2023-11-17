# # 001 Day 46 Goals what you will make by the end of the day
# # 002 Step 1 - Scraping the Billboard Hot 100

import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)
