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
    global volume
    # --- Preparing Terrain Gen ---
    terrain_gen_text_loading_screen = font.render("Starting generation...", True, (205, 140, 205))
    for i in range(random.randint(400, 650)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.fadeout(1)
                t.sleep(1)
                quit()
    
        screen.blit(title_screen_background, (0, 0))
        update_falling_blocks_title_screen()
        draw_falling_blocks_title_screen(screen)
        screen.blit(logo, (115, 50))

        screen.blit(terrain_gen_text_loading_screen, (
            SCREEN_WIDTH // 2 - terrain_gen_text_loading_screen.get_width() // 2,
            SCREEN_HEIGHT // 2 - terrain_gen_text_loading_screen.get_height() // 2))

        pygame.display.flip()
    

    # --- Generating world x by z by y ---
    terrain_gen_text_loading_screen = font.render("Generating " + str(WORLD_SIZE_X) + " by " + str(WORLD_SIZE_Y) + " by " + str(WORLD_SIZE_Z) + " " + default_terrain + " world...", True, (50, 50, 50))
    for i in range(random.randint(800, 1200)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.fadeout(1)
                t.sleep(1)
                quit()
    
        screen.blit(title_screen_background, (0, 0))
        update_falling_blocks_title_screen()
        draw_falling_blocks_title_screen(screen)
        screen.blit(logo, (115, 50))
        screen.blit(terrain_gen_text_loading_screen, (
            SCREEN_WIDTH // 2 - terrain_gen_text_loading_screen.get_width() // 2,
            SCREEN_HEIGHT // 2 - terrain_gen_text_loading_screen.get_height() // 2))

        pygame.display.flip()



    # --- Final touchs ---
    terrain_gen_text_loading_screen = font.render("Applying final touchs!...", True, (100, 255, 100))
    for i in range(random.randint(400, 600)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.fadeout(1)
                t.sleep(1)
                quit()
    
        screen.blit(title_screen_background, (0, 0))
        update_falling_blocks_title_screen()
        draw_falling_blocks_title_screen(screen)
        screen.blit(logo, (115, 50))

        screen.blit(terrain_gen_text_loading_screen, (
            SCREEN_WIDTH // 2 - terrain_gen_text_loading_screen.get_width() // 2,
            SCREEN_HEIGHT // 2 - terrain_gen_text_loading_screen.get_height() // 2))
        
        pygame.display.flip()

    # --- Seed priting ---
    seed_text_loading_screen = font.render("Your world seed is " + str(current_seed), True, (255, 255, 0))
    for i in range(random.randint(500, 700)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.fadeout(1)
                t.sleep(1)
                quit()
    
        screen.blit(title_screen_background, (0, 0))
        update_falling_blocks_title_screen()
        draw_falling_blocks_title_screen(screen)
        screen.blit(logo, (115, 50))

        screen.blit(seed_text_loading_screen, (
            SCREEN_WIDTH // 2 - seed_text_loading_screen.get_width() // 2,
            SCREEN_HEIGHT // 2 - seed_text_loading_screen.get_height() // 2))
        
        pygame.display.flip()
    
    # --- Last Things to be done (Volume fading and stopping everything)
    for i in range(volume):
        volume = max(volume - 1, 0)
        pygame.mixer.music.set_volume(volume / 100)
        running_loading_screen = False
