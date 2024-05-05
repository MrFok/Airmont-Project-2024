from dotenv import load_dotenv
import os
import base64 
from requests import post
import json
import requests

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url,headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_track(token, track_name, artist_name):
    query = f'track:"{track_name}" artist:"{artist_name}"'  # Enclose track and artist names in double quotes
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    params = {
        "q": query,
        "type": "track",
        "limit": 1
    }
    response = requests.get(url, headers=headers, params=params)
    track_info = response.json().get('tracks').get('items')[0]
    return track_info

def get_track_info(token, track_id):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    track_info = response.json()
    return track_info

def get_album_info(token, album_id):
    url = f"https://api.spotify.com/v1/albums/{album_id}"
    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    album_info = response.json()
    return album_info

def get_artist_info(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    artist_info = response.json()
    return artist_info

def search_for_track(token, track_name, artist_name):
    query = f'track:"{track_name}" artist:"{artist_name}"' 
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    params = {
        "q": query,
        "type": "track",
        "limit": 1
    }
    response = requests.get(url, headers=headers, params=params)
    track_info = response.json().get('tracks').get('items')[0]
    return track_info

if __name__ == "__main__":
    track_name = "Wait"
    artist_name = "Maroon 5"
    token = get_token()
    track_info = search_for_track(token, track_name, artist_name)
    print("Track Name:", track_info['name'])
    print("Artist(s):", ", ".join([artist['name'] for artist in track_info['artists']]))
    print("Album:", track_info['album']['name'])
else:
    print("Track not found.")
