import librosa
import librosa.display
import IPython.display as ipd

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

filename = "C:/Users/monke/Projects/Airmont-Project-2024/tests/AmericanIdiot.mp3"

# y is the audio as a waveform, raw data of audio file
# Sampling rate is sr
y, sr = librosa.load(filename)

# tempo and an array of frames when beats occur
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo[0]))

# array of times when beat occured in seconds
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Figure size, line width
pd.Series(y).plot(figsize=(10,5), lw=1, title='Raw Audio Example')
plt.show()

# Zoomed example
# pd.Series(y[1000000:1001000]).plot(figsize=(10,5), lw=1, title='Zoomed Example')
# plt.show()

# Spectrogram

# D = librosa.stft(y)
# S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
# S_db.shape

# fig, ax = plt.subplots(figsize=(10,5))
# img = librosa.display.specshow(S_db, x_axis='time', y_axis='log', ax=ax)
# ax.set_title('Space Cadet Spectrogram Example', fontsize=20)
# fig.colorbar(img, ax=ax, format=f'%0.2f')

# plt.show()
