import pandas as pd
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

pd.set_option('display.max_columns', None)

#TODO: change file path to relative paths. 
country_song_stats = '/Users/uriah/Desktop/repos/ocarina2/Airmont-Project-2024/playlistStats/countrySongs.json'
grunge_song_stats = '/Users/uriah/Desktop/repos/ocarina2/Airmont-Project-2024/playlistStats/grungeSongs.json'
metal_song_stats = '/Users/uriah/Desktop/repos/ocarina2/Airmont-Project-2024/playlistStats/metalSongs.json'
pop_song_stats = '/Users/uriah/Desktop/repos/ocarina2/Airmont-Project-2024/playlistStats/popSongs.json'
rap_song_stats = '/Users/uriah/Desktop/repos/ocarina2/Airmont-Project-2024/playlistStats/rapSongs.json'

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

music_df.to_excel('sample.xlsx')


# music_df.to_excel('countrySongStats.xlsx')
# music_df.to_excel('grunge_song_stats.xlsx')

scaler = MinMaxScaler()
music_features = music_df[['danceability', 'energy', 'loudness', 'speechiness',
                     'acousticness', 'instrumentalness', 'liveness',
                     'valence', 'tempo']]
music_features_scaled = scaler.fit_transform(music_features)

stats_df = pd.DataFrame(music_features_scaled)


def content_based_recommendations(input_song_name, num_recommendations=4):
    if input_song_name not in music_df['name'].values:
        print(f"'{input_song_name}' not found in the dataset. Please enter a valid song name.")
        return
    
    input_song_index = music_df[music_df['name'] == input_song_name].index[0]

    similarity_scores = cosine_similarity([music_features_scaled[input_song_index]], music_features_scaled)

    similar_song_indices = similarity_scores.argsort()[0][::1][1:num_recommendations +1]

    content_based_recommendations = music_df.iloc[similar_song_indices][['name']]

    return content_based_recommendations

input_song_name = input('Input a song name: ')

print(content_based_recommendations(input_song_name, num_recommendations=4))