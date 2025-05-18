#----------------------------------------------------------------------#
# This is the file for the configurations of the game, not be confused
# with config.py
#----------------------------------------------------------------------#

from blocks import *
from random import randint

import pygame
pygame.init()

# --- Player Position and attributes ---
player_pos = [WORLD_SIZE_X - 5, WORLD_SIZE_Y + 3, WORLD_SIZE_Z - 9]
player_rot = [0, 0] # [Yaw, Pitch] in degrees
player_speed: float = 0.2 # (0.2 recommended)
gravity: float = 0 # 0 recommended
player_velocity_y: float = 0
is_jumping: bool = False
jump_height: float = 0

# --- Optional Configurations ---
mouse_sensitivity: float = 0.1 # (0.1)
desired_fps: int = 55
render_distance = 10
starting_volume: int = 100

# --- Terrain Settings ---
default_terrain = "plains"

"""
flatgrass
plains
muddy hills
desert
snowy plains
candyland
caves
"""