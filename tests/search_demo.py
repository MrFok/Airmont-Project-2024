import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipyTest import get_song_features
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

client_id = 'c1691a4a373e4bbc92ffc25525728a07'
client_secret = '63bb642e930b4c698270d0e556fdb6e2'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
	# min_max_values = {
    #     'key': (0, 11),
    #     'loudness': (-60, 0),  # Spotify uses dB scale
    #     'tempo': (0, 250)  # Tempo in beats per minute
    # }
	
	# # Save the values that aren't between (0,1)
	# special_features = {
	# 	'key': features['key'],
	# 	'loudness': features['loudness'],
	# 	'tempo': features['tempo'],
	# }

	# # Initialize and fit the scaler
	# scaler = MinMaxScaler()

	# music_df = pd.DataFrame([features])
	# music_features = music_df[['danceability', 'energy', 'loudness', 'speechiness',
	# 						'acousticness', 'instrumentalness', 'liveness',
	# 						'valence', 'key', 'tempo', 'mode']]
	# scaled_features = scaler.fit_transform(music_features)

	# normalized_features_df = pd.DataFrame(scaled_features, columns=music_features.columns)
	# normalized_features = normalized_features_df.to_dict(orient='list')

	# for feature, (min_val, max_val) in min_max_values.items():
	# 	normalized_features[feature] = (special_features[feature] - min_val) / (max_val - min_val)

def normalizeValues(features):

	normalized_features = {}

	# Replace these min and max values with actual values based on your data
	min_max_values = {

		'danceability': (0, 1),
		'energy': (0, 1),
		'key': (0, 11),
		'loudness': (-60, 0),  # Adjust if necessary
		'mode': (0, 1),
		'speechiness': (0, 1),
		'acousticness': (0, 1),
		'instrumentalness': (0, 1),
		'liveness': (0, 1),
		'valence': (0, 1),
		'tempo': (50, 250)  # Example range, adjust if necessary
	}

	for feature, (min_val, max_val) in min_max_values.items():
		if feature in features:
			# Normalize the feature within its range
			feature_value = features[feature]
			if feature_value < min_val:
				feature_value = min_val
			elif feature_value > max_val:
				feature_value = max_val

			normalized_value = (feature_value - min_val) / (max_val - min_val)
			normalized_features[feature] = normalized_value
	
	return normalized_features

def getRecByFeature(song, limit, hasSameArtist, hasSameGenre):

	# Creates a dictionary with feature as the key and data as the value
	song_features = get_song_features(song)

	norm_song_features = normalizeValues(song_features)
	if norm_song_features:

		# TODO: Normalize the values before calling the recommendations function
		recs = sp.recommendations(
			limit = limit,
			target_danceability = norm_song_features["danceability"],
			target_energy = norm_song_features["energy"],
			target_speechiness = norm_song_features["speechiness"],
			target_acousticness = norm_song_features["acousticness"],
			target_instrumentalness = norm_song_features["instrumentalness"],
			target_liveness = norm_song_features["liveness"],
			target_valence = norm_song_features["valence"],
			target_key = norm_song_features["key"],
			target_mode = norm_song_features["mode"],
		)

		return recs
	else:
		print("No song found for " + song)
		return []


'''
Input: List of songs(max: 5), limit: max number of recommendations
Output: Array of tracks
	Gets recommendations through seed_id
'''
def getRecById(songs, limit):
	
	seed_IDS =  []
	for song in songs:
		result = sp.search(q=song, type="track", limit=1)

		if not result['tracks']['items']:
			continue
		
		# Seed ID of the song if found
		track = result['tracks']['items'][0]
		print(f"Input: {track['name']} by {track['artists'][0]['name']}")

		song_id = track['id']
		seed_IDS.append(song_id)
		
	# returns a list of recommendations
	recommendations = sp.recommendations(seed_tracks=seed_IDS, limit=limit, market="US")
	return recommendations['tracks']



songs = ["Play Ball!", "Blue Honey", "All The Small Things", "Tunnel Vision by Montee lynel", "Nordic Sunrise (Alpha Drone 8Hz)"]
recommendations = getRecById(songs, 5)
for track in recommendations:
	print(f"{track['name']} by {track['artists'][0]['name']}")


# recommendations = getRecByFeature("The Spins by Mac Miller", 5, False, False)

# for track in recommendations:
# 	print(f"{track['name']} by {track['artists'][0]['name']}")
