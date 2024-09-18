import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

def authenticate_spotify():
    # Set your Spotify Developer credentials
    client_id = 'c2cdda865eb74beda36326d10afb50d7'  # Corrected client ID
    client_secret = '66e0c65f22164893a77330df3c8ffad9'

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp

def search_song(sp, title, artist=None):
    query = f'{title}'  # Removed strict 'track:' keyword for more flexibility
    if artist:
        query += f' {artist}'

    # Debug: Show the query being made to Spotify
    print(f"Searching Spotify with query: '{query}'")

    result = sp.search(q=query, type='track', limit=5)  # Increased limit to get more results

    if result['tracks']['items']:
        # List out the first 5 tracks found (limit set to 5)
        for idx, track in enumerate(result['tracks']['items']):
            print(f"{idx+1}. {track['name']} by {track['artists'][0]['name']} - {track['external_urls']['spotify']}")

        # Return the first result
        track = result['tracks']['items'][0]
        print(f"Playing: {track['name']} by {track['artists'][0]['name']}")
        return track['external_urls']['spotify']  # Spotify link to the track
    else:
        print("Song not found!")
        return None

def play_song_spotify(url):
    webbrowser.open(url)

def plays_song(title, artist):
    # Step 1: Authenticate Spotify API
    sp = authenticate_spotify()

    # Step 3: Search for the song on Spotify
    spotify_url = search_song(sp, title, artist)

    if spotify_url:
        play_song_spotify(spotify_url)


