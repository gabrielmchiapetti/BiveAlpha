#-------------------------------------------------------------------------------------------------#
# This is the titlescreen file, containing basic rendering functions for splash texts and others.
#-------------------------------------------------------------------------------------------------#

import time as t
import random
import sys
from os import system as sy

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
from musicplayer import *

pygame.init()

# ----- Title Screen Loop -----
# --- Initializing Pygame ---
initPygame()

# --- Setting texts for the title screen ---
about_text = font.render("Bive " + VERSION + " by Gabriel M. Chiapetti", True, (0, 0, 0))
rect_about_text = about_text.get_rect()
rect_about_text.center = (2 + about_text.get_width() // 2, SCREEN_HEIGHT - about_text.get_height() // 2)

content_start_text = "Singleplayer"
start_text = font.render(content_start_text, True, (255, 255, 255))
rect_start_text = start_text.get_rect()

content_quit_text = "Quit"
quit_text = font.render(" Press ESC to quit ", True, (255, 0, 0))
rect_quit_text = quit_text.get_rect()

volume_text = font.render(" -/+ for volume ", True, (90, 40, 40))

# --- Setting volume and playing music ---
volume = initial_volume

splashtext_rotation = -20

# ----- Falling Blocks on Title Screen -----
# --- Variables ---
falling_blocks_size = 52
falling_blocks_count = 15
falling_blocks_speed = 0.6
falling_blocks = []

# --- Initialize Falling Blocks ---
def initFallingBlocks():
    global falling_blocks
    falling_blocks = []
    block_types = list(BLOCK_COLORS.keys())
    for _ in range(falling_blocks_count):
        block_type = random.choice(block_types)
        color = tuple(int(c * 255) for c in BLOCK_COLORS[block_type][:3])
        x = random.randint(0, SCREEN_WIDTH)
        y = random.uniform(-50, -(SCREEN_HEIGHT + falling_blocks_size + 10))
        falling_blocks.append({'x': x, 'y': y, 'color': color, 'speed': falling_blocks_speed})

# --- Update the falling blocks ---
def updateFallingBlocks():
    for block in falling_blocks:
        block['y'] += block['speed']
        if block['y'] > SCREEN_HEIGHT:
            block['y'] = random.uniform(-50, -1100)
            block['x'] = random.randint(0, 800)
            block_types = list(BLOCK_COLORS.keys())
            block_type = random.choice(block_types)
            block['color'] = tuple(int(c * 255) for c in BLOCK_COLORS[block_type][:3])

# --- Draw the falling blocks to -> surface (screen) ---
def drawFallingBlocks():
    for block in falling_blocks:
        pygame.draw.rect(SCREEN, block['color'], (block['x'], int(block['y']), falling_blocks_size, falling_blocks_size))


# ----- Main Title Screen Loop -----
def titleScreenDo():
    global splashtext_rotation, title_screen_background, start_text, content_start_text, rect_start_text, quit_text, content_quit_text, rect_quit_text, about_text, rect_about_text

    # --- Volume control ---
    volumeControlDo()

    # --- Getting Mouse position ---
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # --- Background Blitting ---
    SCREEN.blit(title_screen_background, (0, 0))
    updateFallingBlocks()
    drawFallingBlocks()

    # --- Blitting logo ---
    SCREEN.blit(logo, ((SCREEN_WIDTH // 2) - logo.get_width() // 2, 50))

    # --- Blitting splash text --
    splash_text_rotated = pygame.transform.rotate(splashtext, splashtext_rotation)
    splashtext_rotation += 0.032

    SCREEN.blit(splash_text_rotated, ((SCREEN_WIDTH // 2) + (logo.get_width() // 3.), 130 - logo.get_height() // 2 + 40))

    # --- Start Text ---
    if rect_start_text.collidepoint(mouse_x, mouse_y):
        start_text = font.render(content_start_text, True, (237, 228, 109))
        rect_start_text = start_text.get_rect()
        rect_start_text.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Center rect
    else:
        start_text = font.render(content_start_text, True, (255, 255, 255))
        rect_start_text = start_text.get_rect()
        rect_start_text.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    SCREEN.blit(start_text, rect_start_text)

    # --- About text ---
    rect_about_text = about_text.get_rect()
    rect_about_text.center = (2 + about_text.get_width() // 2, SCREEN_HEIGHT - about_text.get_height() // 2)

    SCREEN.blit(about_text, rect_about_text)
    
    # --- Quit Text ---
    if rect_quit_text.collidepoint(mouse_x, mouse_y):
        quit_text = font.render(content_quit_text, True, (237, 228, 109))
        rect_quit_text = quit_text.get_rect()
        rect_quit_text.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + start_text.get_height())  # Center rect
    else:
        quit_text = font.render(content_quit_text, True, (255, 255, 255))
        rect_quit_text = quit_text.get_rect()
        rect_quit_text.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + start_text.get_height())

    SCREEN.blit(quit_text, rect_quit_text)

    # --- Volume Text ---
    SCREEN.blit(volume_text, (
        SCREEN_WIDTH // 2 - volume_text.get_width() // 2,
        SCREEN_HEIGHT // 2 - volume_text.get_height() // 2 + start_text.get_height() + (quit_text.get_height() * 2)))
    
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()