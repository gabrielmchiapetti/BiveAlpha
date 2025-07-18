#------------------------------------------------------------#
# This is the file for the defines of Pygame/OpenGl used in
# the main loop
#------------------------------------------------------------#

import pygame

from config import *
from terrain import *
from player import *


# ----- Initialization -----

# --- Init Pygame ---
def initPygame():
    pygame.init()
    pygame_screen = pygame.display.set_mode(((SCREEN_WIDTH, SCREEN_HEIGHT)))
    pygame.display.set_caption(WINDOW_TITLE)
    pygame.display.set_icon(icon)
    pygame.mouse.set_visible(True)
    pygame.event.set_grab(False)
    pygame.font.init()
    pygame.mixer.init()

# --- init OpenGl ---
def initGl():
    # -- Pygame Functions (Do apply to OpenGl) ---
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    # --- Basic OpenGl functions ---
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)  # Enable the discarding of faces not rendered
    glCullFace(GL_BACK)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    # --- OpenGl perspective ---
    glMatrixMode(GL_PROJECTION)
    gluPerspective(fov, (SCREEN_WIDTH / SCREEN_HEIGHT), 0.1, 30.0) # FOV, Aspect Ratio, Near clip, Far clip
    glMatrixMode(GL_MODELVIEW)
    glClearColor(0.6, 0.8, 1.0, 1) # Set Color for sky

    chooseTypeOfTerrain()