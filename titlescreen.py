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

# ----- Falling Blocks on Title Screen -----
# --- Variables ---
falling_blocks_title_screen_size = 42
falling_blocks_title_screen_count = 10
falling_blocks_title_screen_speed = 0.5
falling_blocks_title_screen = []

# --- Initialize Falling Blocks ---
def init_falling_blocks_title_screen():
    global falling_blocks_title_screen
    falling_blocks_title_screen = []
    block_types = list(BLOCK_COLORS.keys())
    for _ in range(falling_blocks_title_screen_count):
        block_type = random.choice(block_types)
        color = tuple(int(c * 255) for c in BLOCK_COLORS[block_type][:3])
        x = random.randint(0, 800)
        y = random.uniform(-50, -1100)
        falling_blocks_title_screen.append({'x': x, 'y': y, 'color': color, 'speed': falling_blocks_title_screen_speed})

# --- Update the falling blocks ---
def update_falling_blocks_title_screen():
    for block in falling_blocks_title_screen:
        block['y'] += block['speed']
        if block['y'] > SCREEN_HEIGHT:
            block['y'] = random.uniform(-50, -1100)
            block['x'] = random.randint(0, 800)
            block_types = list(BLOCK_COLORS.keys())
            block_type = random.choice(block_types)
            block['color'] = tuple(int(c * 255) for c in BLOCK_COLORS[block_type][:3])

# --- Draw the falling blocks to -> surface (screen) ---
def draw_falling_blocks_title_screen(surface):
    for block in falling_blocks_title_screen:
        pygame.draw.rect(surface, block['color'], (block['x'], int(block['y']), falling_blocks_title_screen_size, falling_blocks_title_screen_size))


# ----- Main Title Screen Loop -----
def titleScreenDo():
    global splashtext_rotation, title_screen_background

    # --- Background Blitting ---
    screen.blit(title_screen_background, (0, 0))
    update_falling_blocks_title_screen()
    draw_falling_blocks_title_screen(screen)

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