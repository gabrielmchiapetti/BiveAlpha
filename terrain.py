#---------------------------------------------------------------------#
# This is the file for generating the terrain, and also different
# biomes. default_terrain type is contained on player.py.
#---------------------------------------------------------------------#

import time as t
from perlin_noise import PerlinNoise
import random
import numpy as np
from player import *

from blocks import *
import pygame
pygame.init()

# ------- Terrain & Biome generation -------
# --- Flat Grass World ---
def generateTerrainFlatgrass():
    noise = PerlinNoise(octaves=1, seed=1)
    scale = 1.0 # How much "noisy" is the terrain
    amplitude = 1 # Maximum height of the cliffs

    # --- Add a CLACROCK layer at y = 0 ---
    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            world[x, 0, z] = CLACROCK
    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            # Calculates the height of the world at that point
            height = int(noise([x / scale, z / scale]) * amplitude + (WORLD_SIZE_Y / 2.5)) # Adds an offset
            height = max(1, min(height, WORLD_SIZE_Y - 1)) # Make sure the heights is in its limits

            # Fill the layers
            for y in range(WORLD_SIZE_Y):
                if y < height - 2:
                    world[x, y, z] = STONE
                elif y < height:
                    world[x, y, z] = DIRT
                elif y == height:
                    world[x, y, z] = GRASS
                else:
                    world[x, y, z] = AIR


# --- Plains Biome ---
def generateTerrainPlains():
    noise = PerlinNoise(octaves=4, seed=current_seed)
    scale = 48.0
    amplitude = 8

    # --- Add a CLACROCK layer at y = 0 ---
    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            world[x, 0, z] = CLACROCK

    # --- Terrain generation ---
    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            height = int(noise([x / scale, z / scale]) * amplitude + (WORLD_SIZE_Y / 2.5))
            height = max(1, min(height, WORLD_SIZE_Y - 1))  # clamp height

            for y in range(1, WORLD_SIZE_Y):  # start from y=1 to avoid overwriting CLACROCK
                if y < height - 2:
                    world[x, y, z] = STONE
                elif y < height:
                    world[x, y, z] = DIRT
                elif y == height:
                    world[x, y, z] = GRASS
                else:
                    world[x, y, z] = AIR




# --- Muddy Hill Biome ---
def generateTerrainMuddyHills():
    noise = PerlinNoise(octaves=10, seed=current_seed)
    scale = 48.0
    amplitude = 10

    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            world[x, 0, z] = CLACROCK


    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            height = int(noise([x / scale, z / scale]) * amplitude + (WORLD_SIZE_Y / 2.5))
            height = max(1, min(height, WORLD_SIZE_Y - 1))

            for y in range(1, WORLD_SIZE_Y):
                if y < height - 2:
                    world[x, y, z] = STONE
                elif y < height:
                    world[x, y, z] = STONE
                elif y == height:
                    world[x, y, z] = DIRT
                else:
                    world[x, y, z] = AIR



# --- Desert Biome ---
def generateTerrainDesert():
    noise = PerlinNoise(octaves=3, seed=current_seed)
    scale = 50.0
    amplitude = 8

    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            world[x, 0, z] = CLACROCK
    
    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            height = int(noise([x / scale, z / scale]) * amplitude + (WORLD_SIZE_Y / 2.5))
            height = max(1, min(height, WORLD_SIZE_Y + 3))

            for y in range(1, WORLD_SIZE_Y):
                if y < height - 2:
                    world[x, y, z] = STONE
                elif y < height - 1:
                    world[x, y, z] = random.choice([STONE, SANDSTONE])
                elif y < height:
                    world[x, y, z] = SANDSTONE
                elif y == height:
                    world[x, y, z] = SAND
                else:
                    world[x, y, z] = AIR



# --- Snowy Plains Biome ---
def generateTerrainSnowy_plains():
    noise = PerlinNoise(octaves=3, seed=current_seed)
    scale = 48.0
    amplitude = 10

    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            world[x, 0, z] = CLACROCK

    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            height = int(noise([x / scale, z / scale]) * amplitude + (WORLD_SIZE_Y / 2.5))
            height = max(1, min(height, WORLD_SIZE_Y - 1))

            for y in range(1, WORLD_SIZE_Y):
                if y < height - 1:
                    world[x, y, z] = STONE
                elif y < height:
                    world[x, y, z] = GRASS
                elif y == height:
                    world[x, y, z] = SNOW
                else:
                    world[x, y, z] = AIR

# --- Candyland! :D ---
def generateTerrainCandyland():
    noise = PerlinNoise(octaves=2.5, seed=current_seed)
    scale = 70.0
    amplitude = 6

    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            world[x, 0, z] = CLACROCK

    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            height = int(noise([x / scale, z / scale]) * amplitude + (WORLD_SIZE_Y / 2.5))
            height = max(1, min(height, WORLD_SIZE_Y - 1))

            for y in range(1, WORLD_SIZE_Y):
                if y < height - 1:
                    world[x, y, z] = random.choice([SAND, WOOD])
                elif y < height:
                    world[x, y, z] = SNOW
                elif y == height:
                    world[x, y, z] = CANDY
                else:
                    world[x, y, z] = AIR

# --- Candyland! :D ---
def generateTerrainCaves():
    noise = PerlinNoise(octaves=2.5, seed=current_seed)
    scale = 70.0
    amplitude = 6

    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            world[x, 0, z] = CLACROCK

    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            height = WORLD_SIZE_Y

            for y in range(1, WORLD_SIZE_Y):
                if y < height - 1:
                    world[x, y, z] = random.choice([STONE, AIR, AIR, AIR])
                elif y < height:
                    world[x, y, z] = random.choice([STONE, AIR, AIR, AIR])
                elif y == height:
                    world[x, y, z] = GRASS
                else:
                    world[x, y, z] = AIR

# --- Plains Biome ---
def generateTerrainMossyCaves():
    noise = PerlinNoise(octaves=4, seed=current_seed)
    scale = 48.0
    amplitude = 3

    # --- Add a CLACROCK layer at y = 0 ---
    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            world[x, 0, z] = CLACROCK

    # --- Terrain generation ---
    for x in range(WORLD_SIZE_X):
        for z in range(WORLD_SIZE_Z):
            height = int(noise([x / scale, z / scale]) * amplitude + (WORLD_SIZE_Y / 2.5))
            height = max(1, min(height, WORLD_SIZE_Y - 1))  # clamp height

            for y in range(1, WORLD_SIZE_Y):  # start from y=1 to avoid overwriting CLACROCK
                if y < height - 1:
                    world[x, y, z] = STONE
                elif y < height:
                    world[x, y, z] = MOSS
                elif y < height + 3:
                    world[x, y, z] = AIR
                elif y == height + 4:
                    world[x, y, z] = MOSS
                elif y > height + 4:
                    world[x, y, z] = STONE
                elif y > height + 6:
                    world[x, y, z] = DIRT
                elif y > height + 9:
                    world[x, y, z] = GRASS
                else:
                    world[x, y, z] = AIR

# --- Terrain choosing on the main loop ---
def chooseTypeOfTerrain():
    terrain_map = {
        "flatgrass": generateTerrainFlatgrass,
        "plains": generateTerrainPlains,
        "muddy hills": generateTerrainMuddyHills,
        "desert": generateTerrainDesert,
        "snowy plains": generateTerrainSnowy_plains,
        "candyland": generateTerrainCandyland,
        "caves": generateTerrainCaves,
        "mossy caves": generateTerrainMossyCaves,
    }
    # Usa plains como padrão se não encontrar
    terrain_func = terrain_map.get(default_terrain, generateTerrainPlains)
    terrain_func()