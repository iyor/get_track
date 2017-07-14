#!/env/bin/python3.6
from env import client_id, client_secret
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

song_name = ' '.join(sys.argv[1:])
print("Checking for song:       " + song_name + "\n")
print("Using the following keys: ")
print("ID:          " + client_id)
print("Secret:      " + client_secret)
print("-----------------------------------------------------------------")

search_term = "\"" + '+'.join(sys.argv[1:]) + "\"".lower()

offset = 0

while True:
    results = sp.search(q='track:' + search_term, 
                        offset=offset,
                        limit=50)
    tracks = results["tracks"]["items"]

    if len(tracks) == 0:
        print("Couldn't find that song :(")
        sys.exit()

    for track in tracks:
        if track["name"] == song_name.lower():
            print(track["name"] + "  -  " + track["artists"][0]["name"])
            print(track["uri"])
            sys.exit()
    offset += 50
