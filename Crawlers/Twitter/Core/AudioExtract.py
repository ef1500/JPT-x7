import moviepy.editor as mp
import os
import datetime


def extractMultiAudio():
    path = "./Media/Video/"
    Apath = "./Media/Audio/"
    if not os.path.exists(Apath):
        os.makedirs(Apath)
    for entry in os.scandir(path):
        if entry.path.endswith(".mp4"|".mov"|".webm") and entry.is_file():
            video = mp.VideoFileClip(video)
            video.audio.write_audiofile(Apath + video + ".mp3")
