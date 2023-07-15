# Day 46
# Music Player
# Top 100 songs on my birth date in 1998

CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
REDIRECT_URI = "http://example.com"
URL = "https://www.billboard.com/charts/hot-100/"

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup


# ------------ Spotify authentication -------------- #
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private"))

user_id = sp.current_user()["id"]
print(user_id)

# ------------ Scraping Billboard 100 -------------- #
date = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD: ")
response = requests.get(URL + date)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# ------------ Searching Spotify for songs by title -------------- #
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

# ------------ Creating a new private playlist in Spotify -------------- #
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# ------------ Adding songs found into the new playlist -------------- #
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
