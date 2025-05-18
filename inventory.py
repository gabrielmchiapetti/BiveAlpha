#--------------------------------------#
# This is the file for controling
# inventory/hotbar
#--------------------------------------#

from blocks import *

import pygame
pygame.init()

# --- Simple inventory (Hotbar) ---
hotbar = [GRASS, DIRT, STONE, WOOD, LEAVES, SAND, SANDSTONE, SNOW, CANDY, CLACROCK]
selected_slot = len(hotbar)
inventory = { block: 0 for block in hotbar } # Block counter (Initially 0)