import librosa

filename = librosa.example('nutcracker')

# y is the audio as a waveform
# Sampling rate is sr
y, sr = librosa.load(filename)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo[0]))

beat_times = librosa.frames_to_time(beat_frames, sr=sr)


# msg = "Hello World"
# print(msg)