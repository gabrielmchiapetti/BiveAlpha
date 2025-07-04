#-----------------------------------------------------------------------#
# This is the file for administrating the basic functions of the game,
# like version, width and height of the screen, window title etc.
#-----------------------------------------------------------------------#

import pathlib

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

# --- Initial configurations ---
VERSION: str = "Alpha 1.2.5_a"

BASE_DIR = pathlib.Path(__file__).resolve().parent

SCREEN_WIDTH: int = 1000
SCREEN_HEIGHT: int = 800
WINDOW_TITLE: str = (" Bive " + VERSION + " - github.com/gabrielmchiapetti/BiveAlpha")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(pathlib.Path(BASE_DIR / "Assets" / "Fonts" / "Baskervville-Regular.ttf") , 38)
font_splashtext = pygame.font.Font(pathlib.Path(BASE_DIR / "Assets" / "Fonts" / "Baskervville-Regular.ttf") , 47)
clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# --- Logos and Stuff ---
logo = pygame.image.load(pathlib.Path(BASE_DIR / "Assets" / "Logos" / "carmin.png"))
icon = pygame.image.load(pathlib.Path(BASE_DIR / "Assets" / "Logos" / "icon.ico"))
logo_transform_x: int = 770
logo_transform_y: int = 260
logo = pygame.transform.scale(logo, (logo_transform_x, logo_transform_y))
title_screen_background = pygame.image.load(pathlib.Path(BASE_DIR / "Assets" / "Textures" / "titlescreen.png"))

# ----- Volume Control -----
volume = 100
def volumeControl():
    global volume

    if pygame.key.get_pressed()[pygame.K_EQUALS]:  # '='
        volume = min(volume + 1, 100)
        pygame.mixer.music.set_volume(volume / 100) # Normalize to 0.0 - 1.0

    if pygame.key.get_pressed()[pygame.K_MINUS]: # '+'
        volume = max(volume - 1, 0)
        pygame.mixer.music.set_volume(volume / 100)