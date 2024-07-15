import pandas as pd
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from spotipyTest import get_song_features

pd.set_option('display.max_columns', None)

country_song_stats = '../playlistStats/countrySongs.json'
grunge_song_stats = '../playlistStats/grungeSongs.json'
metal_song_stats = '../playlistStats/metalSongs.json'
pop_song_stats = '../playlistStats/popSongs.json'
rap_song_stats = '../playlistStats/rapSongs.json'

with open(country_song_stats, 'r') as f:
    country_data = json.load(f)

country_df = pd.DataFrame(country_data)

with open(grunge_song_stats, 'r') as f:
    grunge_data = json.load(f)

grunge_df = pd.DataFrame(grunge_data)

with open(metal_song_stats, 'r') as f:
    metal_data = json.load(f)

metal_df = pd.DataFrame(metal_data)

with open(pop_song_stats, 'r') as f:
    pop_data = json.load(f)

pop_df = pd.DataFrame(pop_data)

with open(rap_song_stats, 'r') as f:
    rap_data = json.load(f)

rap_df = pd.DataFrame(rap_data)

music_df = pd.concat([country_df, grunge_df, metal_df, pop_df, rap_df])


# music_df.to_excel('sample.xlsx')

# music_df.to_excel('countrySongStats.xlsx')
# music_df.to_excel('grunge_song_stats.xlsx')

scaler = MinMaxScaler()
music_features = music_df[['danceability', 'energy', 'loudness', 'speechiness',
                     'acousticness', 'instrumentalness', 'liveness',
                     'valence', 'key', 'tempo', 'mode', 'duration']]
music_features_scaled = scaler.fit_transform(music_features)

stats_df = pd.DataFrame(music_features_scaled)

def modified_content_based_recommendations(input_song, num_recommendations=4):

    similarity_scores = cosine_similarity(input_song, music_features_scaled)

    similar_song_indices = similarity_scores.argsort()[0][::-1][1:num_recommendations +1]
    
    content_based_recommendations = music_df.iloc[similar_song_indices][['name', 'artist', 'album']]
    
    return content_based_recommendations

input_song_name = input('Input any song: ')
input_features = get_song_features(input_song_name)

if input_features:

    song_df = pd.DataFrame([input_features])
    print(song_df)
    
    input_song_features = song_df[['danceability', 'energy', 'loudness', 'speechiness',
                                   'acousticness', 'instrumentalness', 'liveness',
                                   'valence', 'key', 'tempo' ,'mode', 'duration']]
    
    scaled_song_df = scaler.transform(input_song_features)
    
    print(modified_content_based_recommendations(scaled_song_df, num_recommendations=2))

else:
    print("No song found")
