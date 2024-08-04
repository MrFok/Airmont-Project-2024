import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from spotipyTest import get_song_features
from createDatabase import get_master_dataframe

main_dataframe = get_master_dataframe()

scaler = MinMaxScaler()
music_features = main_dataframe[['danceability', 'energy', 'loudness', 'speechiness',
                     'acousticness', 'instrumentalness', 'liveness',
                     'valence', 'key', 'tempo', 'mode', 'duration']]
music_features_scaled = scaler.fit_transform(music_features)

music_features_df = pd.DataFrame(music_features_scaled)

stats_df = pd.DataFrame(music_features_scaled)

def modified_content_based_recommendations(input_song, num_recommendations=4):

    similarity_scores = cosine_similarity(input_song, music_features_scaled)

    # sim_scores_df = pd.DataFrame(similarity_scores).to_excel("simScores01.xlsx")

    similar_song_indices = similarity_scores.argsort()[0][::-1][1:num_recommendations +1]

    #print(similar_song_indices)
    
    content_based_recommendations = main_dataframe.iloc[similar_song_indices][['name', 'artist', 'album']]

    similar_song_scaled_stats = music_features_df.iloc[similar_song_indices]
    
    # print(similar_song_scaled_stats)
    similar_song_stats_df = pd.DataFrame(similar_song_scaled_stats)

    # song_recs_df = pd.DataFrame(content_based_recommendations).to_excel("songRecs.xlsx")
    
    return content_based_recommendations, similar_song_stats_df

def get_similar_song_stats(similar_song_stats_df):
    
    return similar_song_stats_df

input_song_name = input('Input any song: ')
input_features = get_song_features(input_song_name)

if input_features:

    song_df = pd.DataFrame([input_features])
    print(song_df)
    
    input_song_features = song_df[['danceability', 'energy', 'loudness', 'speechiness',
                                   'acousticness', 'instrumentalness', 'liveness',
                                   'valence', 'key', 'tempo' ,'mode', 'duration']]
    
    scaled_song_df = scaler.transform(input_song_features)
    
    recommendations, similar_song_stats_df = modified_content_based_recommendations(scaled_song_df, num_recommendations=2)
    
    print(recommendations)
    
    get_similar_song_stats(similar_song_stats_df)
    print(similar_song_stats_df)

else:
    print("No song found")
