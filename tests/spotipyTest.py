import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'c1691a4a373e4bbc92ffc25525728a07'
client_secret = '63bb642e930b4c698270d0e556fdb6e2'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def get_song_statistics(track_id):
    
    track_details = sp.track(track_id)

    audio_features = sp.audio_features(track_id)[0]

    song_statistics = {
        "name": track_details["name"],
        # "artist": track_details["artists"][0]["name"],
        # "album": track_details["album"]["name"],
        # "popularity": track_details["popularity"],
        "danceability": audio_features["danceability"],
        "energy": audio_features["energy"],
        "loudness": audio_features["loudness"],
        "speechiness": audio_features["speechiness"],
        "acousticness": audio_features["acousticness"],
        "instrumentalness": audio_features["instrumentalness"],
        "liveness": audio_features["liveness"],
        "valence": audio_features["valence"],
        "tempo": audio_features["tempo"]
    }

    return song_statistics

def get_playlist_tracks(playlist_id):

    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    return tracks

def print_playlist_stats(playlist_id):
    
    tracks = get_playlist_tracks(playlist_id)

    for item in tracks:
        track = item['track']
        track_id = track['id']
        statistics = get_song_statistics(track_id)
        print(statistics)

playlist_id = '37i9dQZF1EQnqst5TRi17F'
print_playlist_stats(playlist_id)
    

# track_id = '2Foc5Q5nqNiosCNqttzHof'
# statistics = get_song_statistics(track_id)
# print(statistics)