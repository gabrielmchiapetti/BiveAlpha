#----------------------------------------------------------------#
# This is the file for the block managing (IDs, checking, etc.)
# and also for the seed choosing and size of the world
#----------------------------------------------------------------#

import random
import pathlib
import numpy as np

from config import *

pygame.init()

# --- World Size ---
WORLD_SIZE_X = 100
WORLD_SIZE_Y = 20
WORLD_SIZE_Z = 100

current_seed = random.uniform(1.1, 1.9)

# --- World Creation ---
world = np.zeros((WORLD_SIZE_Z, WORLD_SIZE_Y, WORLD_SIZE_X), dtype=float)

# --- IDs of the blocks ---
AIR = 0
GRASS = 1
DIRT = 2
STONE = 3
WOOD = 4
LEAVES = 5
SAND = 6
SNOW = 7
SANDSTONE = 8
CLACROCK = 9
CANDY = 10
CAVEAIR = 11
MOSS = 12
ICE = 13
WATER = 14

# --- Block Colors ---
BLOCK_COLORS = {
    GRASS: (0, 0.8, 0, 1),  # Green
    DIRT: (0.6, 0.4, 0.2, 1), # Brown
    STONE: (0.5, 0.5, 0.5, 1), # Grey
    WOOD: (0.7, 0.5, 0.3, 1), # Bright Brown
    LEAVES: (0.2, 0.6, 0.1, 1), # Dark Green
    SAND: (0.917, 0.882, 0.690, 1), # Sand Color
    SNOW: (0.970, 0.980, 0.995, 1), # White
    SANDSTONE: (0.898, 0.847, 0.564, 1), # Dark sand color
    CLACROCK: (0.150, 0.1, 0.1, 1 ), # Redish Black
    CANDY: (1.0, 0.412, 0.706, 1 ), # Pink!
    CAVEAIR: (0.1, 0.1, 0.1, 0.0), # Transparent, made to be a alternative to air, doesn't appear on the hotbar
    MOSS: (0, 0.3, 0 , 1), # Dark Green
    ICE: (0, 0.8, 1, 0.2), # Light Aqua
    WATER: (0.1, 0.1, 1, 0.4) # Darkish Blue
}

# --- Seed choosing function ---
def randomSeed():
    current_seed = random.uniform(1.0001, 1.9999)

# --- Block checking functions ---
def getBlock(z, y, x):
    x, y, z = int(round(x)), int(round(y)), int(round(z))
    if 0 <= x < WORLD_SIZE_X and 0 <= y < WORLD_SIZE_Y and 0 <= z < WORLD_SIZE_Z:
        return world[x, y, z]
    return AIR

def setBlock(z, y, x, block_type):
    x, y, z = int(round(x)), int(round(y)), int(round(z))
    if 0 <= x < WORLD_SIZE_X and 0 <= y < WORLD_SIZE_Y and 0 <= z < WORLD_SIZE_Z:
        world[x, y, z] = block_type

def isBlockExposedToAir(z, y, x):
    # Check the 6 block neighbours
    adjacents = [
        getBlock(x+1, y, z), getBlock(x-1, y, z),
        getBlock(x, y+1, z), getBlock(x, y-1, z),
        getBlock(x, y, z+1), getBlock(x, y, z-1)
    ]
    return AIR in adjacents