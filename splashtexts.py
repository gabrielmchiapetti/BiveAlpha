#------------------------------------------------------------------------------------------#
# This is the script for reading and choosing splash texts from the splashtexts.txt file,
# Thanks for the idea Notch!
#------------------------------------------------------------------------------------------#
import random
import pygame
import pathlib

from config import *

pygame.init()

# --- Opening and selecting the Splash Texts ---
splashtext_file_path = pathlib.Path(BASE_DIR / "Assets" / "Others" / "splashtexts.txt")
selected_splashtext = None
with open(splashtext_file_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        if random.randrange(i) == 0:
            selected_splashtext = line.strip()

# --- Setting up splash text basics ---
splashtext = font_splashtext.render(selected_splashtext, True, (0, 255, 0))
splashtext_rotation = -20
splashtext_rotated = pygame.transform.rotate(splashtext, splashtext_rotation)
splashtext_pulse_direction = 1