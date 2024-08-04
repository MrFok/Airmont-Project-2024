import pandas as pd
import json

def open_json_files():

    file_paths = {
        'country': '../playlistStats/countrySongs.json',
        'grunge': '../playlistStats/grungeSongs.json',
        'metal': '../playlistStats/metalSongs.json',
        'pop': '../playlistStats/popSongs.json',
        'rap': '../playlistStats/rapSongs.json'
    }

    dataframes = {}
    for genre, file_path in file_paths.items():
        with open(file_path, 'r') as f:
            data = json.load(f)
        dataframes[genre] = pd.DataFrame(data)
    
    return dataframes

def create_master_dataframe(dataframes):

    master_df = pd.concat(dataframes.values(), ignore_index=True)

    return(master_df)


#TODO: Create a function to save dataframe as a csv file
#      update get_master_dataframe to retrieve saved database
def get_master_dataframe():
    dataframes = open_json_files()
    master_df = create_master_dataframe(dataframes)
    return master_df

master_df = get_master_dataframe()
# print(master_df)

