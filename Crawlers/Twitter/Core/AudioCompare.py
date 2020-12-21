#This will find similar audio
# Subprocess:
#   1) Split audio into lots of different parts
#   2) Test the snippet against every single segment of the target's audio
#   3) Provide a similarity result in the form of a precentage.

import numpy as np
import matplotlib.pyplot as plt
import librosa

path = "./Media/Audio/"

def analzyeAudio():
    for entry in os.scandir(path):
        if entry.path.endswith(".mp3") and entry.is_file():
            load(entry, sr=none, mono=true, duration=7, dtype=float32)
