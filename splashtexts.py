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
open_splashtexts = open(pathlib.Path(BASE_DIR / "Assets" / "Others" / "splashtexts.txt")).read().splitlines()
selected_splashtext = random.choice(open_splashtexts)
# --- Setting up splash text basics ---
splashtext_font = pygame.font.Font(pathlib.Path(BASE_DIR / "Assets" / "Fonts" / "Baskervville-Regular.ttf"), 40)
splashtext = splashtext_font.render(selected_splashtext, True, (0, 255, 0))
splashtext_rotated = pygame.transform.rotate(splashtext, -20)
splashtext_initial_rotation: float = -20
splashtext_initial_font_size = 40

splashtext_font_size = splashtext_initial_font_size  # These goes here, so python can detect their are not repeated
splashtext_rotation = splashtext_initial_rotation
splashtext_rotated = pygame.transform.rotate(splashtext, splashtext_rotation)
splashtext_pulse_direction = 1