#------------------------------------------------------------------------#
# This is the file for the loading screen, or "World generation" screen
# P.S. It is a placebo effect, all the terrain generation is done on
# the OpenGl window, added it for cosmetic looks.
#------------------------------------------------------------------------#

import time as t
import random

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
from titlescreen import *

# --- Loading Screen loop ---
volume = initial_volume
def loadingScreenDo():
    global volume, splashtext, splashtext_rotated, selected_splashtext, splashtext_rotation
    # --- Preparing Terrain Gen ---
    current_terrain_gen_text = font.render("Starting generation...", True, (255, 100, 255))
    for i in range(random.randint(400, 650)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.fadeout(1)
                t.sleep(1)
                sys.exit()
    
    # --- Blitting cosmetics ---
        SCREEN.blit(title_screen_background, (0, 0))

        updateFallingBlocks()
        drawFallingBlocks()

        SCREEN.blit(logo, ((SCREEN_WIDTH // 2) - logo.get_width() // 2, 50))

        if i < 360:
            splashtext_rotation += 360 / 360
        else:
            splashtext_rotation += 0.032  # rotação normal

        splash_text_rotated = pygame.transform.rotate(splashtext, splashtext_rotation)
        splashtext_rotation += 0.032
        SCREEN.blit(splash_text_rotated, ((SCREEN_WIDTH // 2) + (logo.get_width() // 3.), 130 - logo.get_height() // 2 + 40))

        SCREEN.blit(current_terrain_gen_text, (
            SCREEN_WIDTH // 2 - current_terrain_gen_text.get_width() // 2,
            SCREEN_HEIGHT // 2 - current_terrain_gen_text.get_height() // 2))

        pygame.display.flip()
    

    # --- Generating world x by z by y ---
    current_terrain_gen_text = font.render("Generating " + str(WORLD_SIZE_X) + " by " + str(WORLD_SIZE_Y) + " by " + str(WORLD_SIZE_Z) + " " + default_terrain + " world...", True, (50, 50, 50))
    for i in range(random.randint(400, 550)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.fadeout(1)
                t.sleep(1)
                sys.exit()
    
        SCREEN.blit(title_screen_background, (0, 0))

        updateFallingBlocks()
        drawFallingBlocks()

        SCREEN.blit(logo, ((SCREEN_WIDTH // 2) - logo.get_width() // 2, 50))

        splash_text_rotated = pygame.transform.rotate(splashtext, splashtext_rotation)
        splashtext_rotation += 0.032
        SCREEN.blit(splash_text_rotated, ((SCREEN_WIDTH // 2) + (logo.get_width() // 3.), 130 - logo.get_height() // 2 + 40))

        SCREEN.blit(current_terrain_gen_text, (
            SCREEN_WIDTH // 2 - current_terrain_gen_text.get_width() // 2,
            SCREEN_HEIGHT // 2 - current_terrain_gen_text.get_height() // 2))

        pygame.display.flip()



    # --- Final touchs ---
    current_terrain_gen_text = font.render("Applying final touchs!...", True, (100, 255, 100))
    for i in range(random.randint(200, 300)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.fadeout(1)
                t.sleep(1)
                sys.exit()
    
        SCREEN.blit(title_screen_background, (0, 0))

        updateFallingBlocks()
        drawFallingBlocks()

        SCREEN.blit(logo, ((SCREEN_WIDTH // 2) - logo.get_width() // 2, 50))

        splash_text_rotated = pygame.transform.rotate(splashtext, splashtext_rotation)
        splashtext_rotation += 0.032
        SCREEN.blit(splash_text_rotated, ((SCREEN_WIDTH // 2) + (logo.get_width() // 3.), 130 - logo.get_height() // 2 + 40))

        SCREEN.blit(current_terrain_gen_text, (
            SCREEN_WIDTH // 2 - current_terrain_gen_text.get_width() // 2,
            SCREEN_HEIGHT // 2 - current_terrain_gen_text.get_height() // 2))
        
        pygame.display.flip()

    # --- Seed priting ---
    seed_text_loading_screen = font.render("Your world seed is " + str(current_seed), True, (255, 255, 0))
    for i in range(random.randint(500, 680)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.fadeout(1)
                t.sleep(1)
                sys.exit()
    
        SCREEN.blit(title_screen_background, (0, 0))

        updateFallingBlocks()
        drawFallingBlocks()

        SCREEN.blit(logo, ((SCREEN_WIDTH // 2) - logo.get_width() // 2, 50))

        splash_text_rotated = pygame.transform.rotate(splashtext, splashtext_rotation)
        splashtext_rotation += 0.032
        SCREEN.blit(splash_text_rotated, ((SCREEN_WIDTH // 2) + (logo.get_width() // 3.), 130 - logo.get_height() // 2 + 40))

        SCREEN.blit(seed_text_loading_screen, (
            SCREEN_WIDTH // 2 - seed_text_loading_screen.get_width() // 2,
            SCREEN_HEIGHT // 2 - seed_text_loading_screen.get_height() // 2))
        
        pygame.display.flip()
    
    # --- Last Things to be done (Volume fading and stopping everything)
    for i in range(volume):
        volume = max(volume - 1, 0)
        pygame.mixer.music.set_volume(volume / 100)
        running_loading_screen = False
