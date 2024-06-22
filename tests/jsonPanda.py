import pandas as pd
import json

pd.set_option('display.max_columns', None)

country_song_stats = '/Users/uriah/Desktop/repos/ocarina2/Airmont-Project-2024/playlistStats/countrySongs.json'

with open(country_song_stats, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df.to_excel('countrySongStats.xlsx')