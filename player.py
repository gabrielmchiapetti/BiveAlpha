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

# ----- Reading the options from the options.txt file -----

# --- Reading the file ---
with open(pathlib.Path(BASE_DIR / "Options" / "options.txt")) as open_options:
    read_options = [line.strip() for line in open_options if line.strip()]

# --- Assign the lines values to the variables ---
mouse_sensitivity = float(read_options[12])
desired_fps = float(read_options[13])
render_distance = int(read_options[14])
fov = float(read_options[15])
initial_volume = int(read_options[16])
default_terrain = str(read_options[17])