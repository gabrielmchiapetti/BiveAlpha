#-------------------------------------------------------------------------------------------------#
# This is the titlescreen file, containing basic rendering functions for splash texts and others.
#-------------------------------------------------------------------------------------------------#

import os
from os import system as sy
import time as t
import math
from datetime import datetime
from typing import Final
import random
import pathlib

import pygame

# --- Importing from the other files ---
from blocks import *
from player import *
from inventory import *
from graphics import *
from config import *
from terrain import *
from splashtexts import *
from initialize import *

pygame.init()

# ----- Title Screen Loop -----
# --- Initializing Pygame ---
initPygame()

# --- Setting texts for the title screen ---
about_text_title_screen = font.render("Bive " + VERSION + " by Gabriel M. Chiapetti", True, (0, 0, 0))
start_text_title_screen = font.render("> Press RETURN to play <", True, (255, 255, 255))
quit_text_title_screen = font.render("> Press ESC to quit <", True, (255, 0, 0))
volume_text_title_screen = font.render("> -/+ for volume <", True, (90, 40, 40))

# --- Setting volume and playing music ---
volume = starting_volume

splashtext_rotation = splashtext_initial_rotation

def titleScreenDo():
    global splashtext_rotation
    # --- Background Blitting ---
    screen.blit(title_screen_background, (0, 0))

    # --- Blitting logo ---
    screen.blit(logo, (115, 50))

    # --- Blitting splash text --
    splash_text_rotated = pygame.transform.rotate(splashtext, splashtext_rotation)
    splashtext_rotation += 0.025

    screen.blit(splash_text_rotated, (385 + logo.get_width() - 425, 130 - logo.get_height() // 2 + 40))

    # --- About text ---
    screen.blit(about_text_title_screen, (1, SCREEN_HEIGHT -about_text_title_screen.get_height()))

    # --- Start text ---
    screen.blit(start_text_title_screen, (
        SCREEN_WIDTH // 2 - start_text_title_screen.get_width() // 2,
        SCREEN_HEIGHT // 2 - start_text_title_screen.get_height() // 2))
    
    # --- Quitting Text ---
    screen.blit(quit_text_title_screen, (
        SCREEN_WIDTH // 2 - quit_text_title_screen.get_width() // 2,
        SCREEN_HEIGHT // 2 - quit_text_title_screen.get_height() // 2 + start_text_title_screen.get_height()))

    # --- Volume Text ---
    screen.blit(volume_text_title_screen, (
        SCREEN_WIDTH // 2 - volume_text_title_screen.get_width() // 2,
        SCREEN_HEIGHT // 2 - volume_text_title_screen.get_height() // 2 + start_text_title_screen.get_height() + (quit_text_title_screen.get_height() * 2)))

    
    # ----- Key Pressing detection -----
    volume_control()
    
    # --- Quitting and Generating keys detection ---
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        pygame.mixer.music.load(pathlib.Path("Assets/Audios/cluckout.mp3"))
        pygame.mixer.music.play()
        t.sleep(0.2)
        quit()

    # --- Quitting ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            for i in volume():
                volume -= 1
            quit()

    pygame.display.flip()