#-----------------------------------------------------------------------#
# This is the file for administrating the basic functions of the game,
# like version, width and height of the screen, window title etc.
#-----------------------------------------------------------------------#

import pathlib
import datetime

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

# --- Initial configurations ---
VERSION: str = "Alpha 1.2.6"

BASE_DIR = pathlib.Path(__file__).resolve().parent

SCREEN_WIDTH: int = 1100
SCREEN_HEIGHT: int = 900
WINDOW_TITLE: str = (" Bive " + VERSION + " - github.com/gabrielmchiapetti/BiveAlpha")
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WEBSITE = "https://github.com/gabrielmchiapetti/BiveAlpha"

font = pygame.font.Font(pathlib.Path(BASE_DIR / "Assets" / "Fonts" / "Baskervville-Regular.ttf") , 44)
font_splashtext = pygame.font.Font(pathlib.Path(BASE_DIR / "Assets" / "Fonts" / "Baskervville-Regular.ttf"), 35)

clock = pygame.time.Clock()
mouse_x, mouse_y = pygame.mouse.get_pos()

datetime = datetime.datetime.now()
datetime_now = datetime.strftime('%H-%M-%S %Y-%m-%d')


# --- Logos and Stuff ---
logo = pygame.image.load(pathlib.Path(BASE_DIR / "Assets" / "Logos" / "carmin.png"))
icon = pygame.image.load(pathlib.Path(BASE_DIR / "Assets" / "Logos" / "icon.ico"))
logo = pygame.transform.scale2x(logo)
title_screen_background = pygame.image.load(pathlib.Path(BASE_DIR / "Assets" / "Textures" / "titlescreen.png"))

# ----- Volume Control -----
volume = 100
def volumeControlDo():
    global volume

    if pygame.key.get_pressed()[pygame.K_EQUALS]:  # '='
        volume = min(volume + 1, 100)
        pygame.mixer.music.set_volume(volume / 100) # Normalize to 0.0 - 1.0

    if pygame.key.get_pressed()[pygame.K_MINUS]: # '+'
        volume = max(volume - 1, 0)
        pygame.mixer.music.set_volume(volume / 100)