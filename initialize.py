#------------------------------------------------------------#
# This is the file for the defines of Pygame/OpenGl used in
# the main loop
#------------------------------------------------------------#

import pygame
import time as t

from config import *
from terrain import *


# ----- Initialization -----

# --- Init Pygame ---
def initPygame():
    pygame.init()
    pygame_screen = pygame.display.set_mode(((SCREEN_WIDTH, SCREEN_HEIGHT)), pygame.RESIZABLE)
    pygame.display.set_caption(WINDOW_TITLE)
    pygame.display.set_icon(icon)
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)
    pygame.font.init()
    pygame.mixer.init()

# --- init OpenGl ---
def initGl():
    # --- Basic OpenGl functions ---
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)  # Enable the discarding of faces not rendered
    glCullFace(GL_BACK)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    # --- OpenGl perspective ---
    glMatrixMode(GL_PROJECTION)
    gluPerspective(70, (SCREEN_WIDTH / SCREEN_HEIGHT), 0.1, 100.0) # FOV, Aspect Ratio, Near clip, Far clip
    glMatrixMode(GL_MODELVIEW)
    glClearColor(0.6, 0.8, 1.0, 1) # Set Color for sky

    chooseTypeOfTerrain()