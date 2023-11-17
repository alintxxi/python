# # 001 Day 46 Goals what you will make by the end of the day
# # 002 Step 1 - Scraping the Billboard Hot 100

import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_spans]


# # 003 Step 2 - Authentication with Spotify
Client_ID = "f7590b25b02b462ebe0fdcb9963a9c7e"
Client_secret = "de32a02a87c14c8ba55e383ba1be8f4e"

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=Client_ID,
        client_secret=Client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
# https://example.com/?code=AQDeF3QLCrjEByPykhi24FxykDSf6eUFRy2Wpz2-qzs5ca_o5JTGJljLQMTG75YQzmSHOSDV2raMdhFLuCTJq-pMMad1Z6g0phnE-TmLLizvSYGmyZZL0r1FC3ry0PSmYydkQ37_CBlYoNIuZGeZMr0hP50eaRqGtjLBSmLwX9jEeBh6Bi65Myn95gzBe9IN
user_id = sp.current_user()["id"]


# # 004 Step 3 - Search Spotify for the Songs from Step 1
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
