from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

client_id = "4f6d4c15e7b74291ab61832404262d94"
secret_id = "d013c9a775414693be1c060538693948"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=secret_id,
        redirect_uri="http://localhost:8888/callback",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
)
)
#{'display_name': 'Akash', 'external_urls': {'spotify': 'https://open.spotify.com/user/b5351can4x1opy5eso51lpymr'}, 'followers': {'href': None, 'total': 0}, 'href': 'https://api.spotify.com/v1/users/b5351can4x1opy5eso51lpymr', 'id': 'b5351can4x1opy5eso51lpymr', 'images': [], 'type': 'user', 'uri': 'spotify:user:b5351can4x1opy5eso51lpymr'}
user_id = sp.current_user()
print(f"user_id = {user_id}")

date = input("Which year would you like to travel to?!\nEnter time in YYYY-MM-DD format: ")
year = date.split("-")[0]

endpoint = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url=endpoint)
soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify())

songs_list = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

songs = [song.getText() for song in songs_list]
print(songs)

songs_uri = []
for song in songs:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        #pprint(result)
        try:
                uri = result["tracks"]["items"][0]["uri"]
                songs_uri.append(uri)
        except IndexError:
                print(f"'{song}': Doesn't exist in Spotify. Skipped.")

user_id = user_id["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uri)