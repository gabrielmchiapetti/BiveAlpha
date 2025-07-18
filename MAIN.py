#----------------------------------------------------------------------------------------#
# >>> Bive Alpha 1.2.6
# >>> Made by Gabriel M. Chiapetti (@gabrielmchiapetti on github)
#
# This is the main file, RUN FROM HERE, make sure that the other parts are present too.
#----------------------------------------------------------------------------------------#

# -> This is the Main application, piecing all of the other files and itself apart
# to make the game.


# --- Basic Dependencies, already comes with python ---
import os
import subprocess
import sys
import time as t
import math
import webbrowser

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# --- Import the dependecies, if it's not possible, will try downloading them via pip ---
try:
	import pygame
except Exception:
        print("Downloading dependencies (pygame)...")
        t.sleep(0.5)
        subprocess.call("pip3 install pygame --break-system-packages", shell=True) # --break-system-packages is needed for resolving the "Device is externally managed" pip problem 
t.sleep(5)                                                                         # (there is no other way around)
import pygame
from pygame.locals import *

try:
	import numpy
except Exception:
        print("Downloading dependencies (numpy)...")
        t.sleep(0.5)
        subprocess.call("pip3 install numpy --break-system-packages", shell=True)
import numpy

try:
	import perlin_noise
except Exception:
        print("Downloading dependencies (perlin_noise)...")
        t.sleep(0.5)
        subprocess.call("pip3 install perlin_noise --break-system-packages", shell=True)
import perlin_noise

try:
	import OpenGL
except Exception:
        print("Downloading dependencies (PyOpenGl)...")
        t.sleep(0.5)
        subprocess.call("pip3 install PyOpenGl --break-system-packages", shell=True)
from OpenGL.GL import *
from OpenGL.GLU import *

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
from loadingscreen import *
from musicplayer import *

# --- Initializing Pygame ---
initPygame()

# ----- Title Screen Loop -----
splashtext_rotation = -20

# --- Music and Sound Effects ---
volume = initial_volume
pygame.mixer.music.set_volume(initial_volume)
pygame.mixer.music.load(sound_cluckin)
pygame.mixer.music.play()

pygame.mixer.music.load(music_grand_opening)
pygame.mixer.music.play()

# --- Setting the cursor ---
pygame.mouse.set_cursor(*pygame.cursors.tri_left)

# ----- Title Screen loop -----
running_title = True
initFallingBlocks()
while running_title:
    clock.tick(100)
    
    titleScreenDo()

    rect_start_text.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    rect_quit_text.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + start_text.get_height())

    # --- Mouse positioning and button checking ---
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()

    # --- Clickable Menus ---
    if mouse_buttons[0]:  # Left Mouse button
        if rect_start_text.collidepoint(mouse_x, mouse_y):
            running_title = False
        if rect_quit_text.collidepoint(mouse_x, mouse_y):
            pygame.mixer.Sound(sound_cluckout)
            t.sleep(0.2)
            pygame.quit()
            sys.exit()
        if rect_about_text.collidepoint(mouse_x, mouse_y):
            webbrowser.open(WEBSITE)

    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# ----- Loading Screen loop -----
running_loading_screen = True
while running_loading_screen:

    loadingScreenDo()
    for i in range(volume):
        volume = max(volume - 1, 0)
        pygame.mixer.music.set_volume(volume / 100)
        running_loading_screen = False


# --- Starting OpenGl (Needs to be done here) ---
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
initGl()

# --- Stopping Pygame Mixer ---
pygame.mixer.music.stop()

# ----- Main Game loop ------
running = True
while running:

    # --- Controling FPS ---
    clock.tick(desired_fps)

    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Mouse movement (Camera) ---
    dx, dy = pygame.mouse.get_rel()
    player_rot[0] += dx * mouse_sensitivity
    player_rot[1] += dy * mouse_sensitivity
    player_rot[1] = max(-89, min(89, player_rot[1])) # Limits vertica angle

    # --- Keyboard handling  ---
    move_vec = [0, 0, 0] #Front/Back, Top/Bottom, Left/Right
    if pygame.key.get_pressed()[pygame.K_w]:
        move_vec[0] -= 1
    if pygame.key.get_pressed()[pygame.K_s]:
        move_vec[0] += 1
    if pygame.key.get_pressed()[pygame.K_a]:
        move_vec[2] -= 1
    if pygame.key.get_pressed()[pygame.K_d]:
        move_vec[2] += 1
    if pygame.key.get_pressed()[pygame.K_LSHIFT]:
        move_vec[1] -= 1
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        move_vec[1] += 1
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        running = False

    # --- Horizontal Movement ---
    if move_vec[0] != 0 or move_vec[2] != 0:
        # Normalize horizontal movement vector for not walking diagonally faster
        angle = math.radians(player_rot[0])
        move_len = math.sqrt(move_vec[0]**2 + move_vec[2]**2)
        norm_fwd = move_vec[0] / move_len
        norm_side = move_vec[2] / move_len

        # Calculate movement based on camera (Please don't change this)
        final_dx = (-norm_fwd * math.cos(angle) + -norm_side * math.sin(angle)) * player_speed
        final_dz = (norm_fwd * math.sin(angle) + -norm_side * math.cos(angle)) * player_speed


        # --- Horizontal Movement ---
        player_pos[0] -= final_dx  # X-axis (left/right)
        player_pos[2] -= final_dz  # Z-axis (forward/backward)
    # --- Vertical movement ---
    new_pos_y = player_pos[1] + move_vec[1] * player_speed * 0.8  # Y movement (scaled a bit)
    player_pos[1] = new_pos_y


    # --- Rendering ---
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glRotatef(player_rot[1], 1, 0, 0) # Vertical rotation (Pitch)
    glRotatef(player_rot[0], 0, 1, 0) # Horizontal rotation (Yaw)
    glTranslatef(-player_pos[2], -player_pos[1], -player_pos[0]) # Camera Translation

    drawWorld()

    if pygame.key.get_pressed()[pygame.K_e]:
        drawHotbar()

    drawCrosshair()

    pygame.display.flip()

sys.exit()