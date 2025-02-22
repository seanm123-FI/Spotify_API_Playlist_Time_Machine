import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


SPOTIPY_CLIENT_ID='' #Insert your ID here
SPOTIPY_CLIENT_SECRET='' #Insert your Secret here
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope,
                                               cache_path= "token.txt"))

# Get current user information
user = sp.current_user()
print(f"Logged in as: {user['display_name']}")

URL = ('https://www.billboard.com/charts/hot-100/')

user_input = input('Which year do you want to travel to? Type the date in this format (YYYY-MM-DD):')

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

total_URL = URL + user_input
response = requests.get(total_URL, headers=header)
billboard_website_html = response.text

soup = BeautifulSoup(billboard_website_html, 'html.parser')

#soup = BeautifulSoup(response.text, 'html.parser')
song_titles = soup.find_all('h3',class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

songs_list=[songs.get_text(strip=True) for songs in song_titles]

song_uris = []

year = user_input.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

create_playlist = sp.user_playlist_create(user["id"], name = f"{user_input} Billboard 100", public=False, collaborative=False, description='')
sp.playlist_add_items(playlist_id=create_playlist["id"], items = song_uris)


pprint(song_uris)
print(songs_list)