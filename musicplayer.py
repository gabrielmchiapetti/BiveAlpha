#------------------------------------------------------#
# This is the file for music playing in the game loop
# (NOT ON TITLE SCREEN/LOADING SCREEN!!!)
#------------------------------------------------------#
import random

import pygame

from config import *

# --- Setting everything up ---
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

# --- All of the Sound Effects ---
sound_cluckin = pathlib.Path(BASE_DIR / "Assets" / "Audios" / "cluckin.mp3")
sound_cluckout = pathlib.Path(BASE_DIR / "Assets" / "Audios" / "cluckout.mp3")

all_sounds = [sound_cluckin, sound_cluckout]

# --- All of the music ---
music_grand_opening = pathlib.Path(BASE_DIR / "Assets" / "Audios" / "grand_opening.mp3")
music_alpha = pathlib.Path(BASE_DIR / "Assets" / "Audios" / "alpha.mp3")

all_musics = [music_grand_opening, music_alpha]


# --- Main function ---
def playMusic():

    if not pygame.mixer.music.get_busy():
        print(volume)
        if random.randint(1, 200) == 1:
            track_path = str(random.choice(all_musics))
            pygame.mixer.music.load(track_path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play()