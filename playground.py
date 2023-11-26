import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


os.environ["SPOTIPY_CLIENT_ID"] = "7777ac4f09a747a1ab0f0e1cef7a2323"
os.environ["SPOTIPY_CLIENT_SECRET"] = "11cf4026d8084e4ca99081bb8c2f93cd"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:9000"
scope = "user-library-read user-library-modify playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
print("---User Info---")
user = sp.current_user()
user_id = user["id"]
print("User's ID:", user_id)
print("User's name:", user["display_name"])
print("User's followers:", user["followers"]["total"])

print("---User Playlist---")
# user_playlists = sp.user_playlists(user=user_id, limit=10)
current_user_playlists = sp.current_user_playlists(limit=10)
print(current_user_playlists["items"][0].keys())
for p in current_user_playlists["items"]:
    print("Playlist's name:", p["name"])
    print("Playlist's owner:", p["owner"]["display_name"])
    print()

# Create new playlist
# new_playlist = sp.user_playlist_create(user=user_id, name="My New Playlist", public=True, collaborative=False, description="Created using Spotipy")
# print("---New Playlist Info---")
# print("Playlist's ID:", new_playlist["id"])
# print("Keys:", new_playlist.keys())
# print("Name:", new_playlist["name"])
# print("Description:", new_playlist["description"])
# print("Total tracks", new_playlist["tracks"]["total"])

# Add songs to my new playlist
# star_gazing_song_uri = "spotify:track:0VF7YLIxSQKyNiFL3X6MmN"
# sweater_weather_song_url = "spotify:track:2QjOHCTQ1Jl3zawyYOpxh6?si=0af53807a6084782"
# song1 = "spotify:track:16XswZ18xhMs8qUTN51mRl"
# new_playlist = sp.playlist_add_items(playlist_id=new_playlist["id"], items=["spotify:track:4iV5W9uYEdYUVa79Axb7Rh","spotify:track:1301WleyT98MSxVHPZCA6M"], position=None)

