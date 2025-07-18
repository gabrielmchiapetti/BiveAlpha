#-----------------------------------------------------------------------------#
# This is the file that contains the definition for the graphics, like cubes,
# normals, drawing hotbar and etc.
#-----------------------------------------------------------------------------#

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

from blocks import *
from config import *
from inventory import *
from player import *

pygame.init()

# ------- Cube Drawing -------
def drawCube(z, y, x, block_type):
    if block_type == AIR or not isBlockExposedToAir(z, y, x):
        return

    vertices = [
        [-0.5, -0.5,  0.5], [ 0.5, -0.5,  0.5], [ 0.5,  0.5,  0.5], [-0.5,  0.5,  0.5],
        [-0.5, -0.5, -0.5], [-0.5,  0.5, -0.5], [ 0.5,  0.5, -0.5], [ 0.5, -0.5, -0.5],
        [-0.5,  0.5,  0.5], [ 0.5,  0.5,  0.5], [ 0.5,  0.5, -0.5], [-0.5,  0.5, -0.5],
        [-0.5, -0.5,  0.5], [-0.5, -0.5, -0.5], [ 0.5, -0.5, -0.5], [ 0.5, -0.5,  0.5],
        [ 0.5, -0.5,  0.5], [ 0.5, -0.5, -0.5], [ 0.5,  0.5, -0.5], [ 0.5,  0.5,  0.5],
        [-0.5, -0.5,  0.5], [-0.5,  0.5,  0.5], [-0.5,  0.5, -0.5], [-0.5, -0.5, -0.5]
    ]

    faces = [
        [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11],
        [12, 13, 14, 15], [16, 17, 18, 19], [20, 21, 22, 23]
    ]

    normals = [
        [0, 0, 1], [0, 0, -1], [0, 1, 0],
        [0, -1, 0], [1, 0, 0], [-1, 0, 0]
    ]

    glPushMatrix()
    glTranslatef(x + 0.5, y + 0.5, z + 0.5)
    glColor4fv(BLOCK_COLORS.get(block_type, (1, 1, 1)))

    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        nx, ny, nz = normals[i]
        if getBlock(x + nx, y + ny, z + nz) == AIR:
            glNormal3f(nx, ny, nz)
            for idx in face:
                glVertex3f(*vertices[idx])
    glEnd()

    glPopMatrix()


# ----- World Drawing -----
def drawWorld(): # r-squared + single-int algorithm
    
    px, py, pz = map(int, player_pos) # Converts it all to int right away 
    r = render_distance

    r_squared = r * r # r-squared, sqrt() or ** is too memory expensive, so
    # we use this basic 1st grade math technique!

    for dx in range(-r, r + 1):
        x = px + dx
        if x < 0 or x >= WORLD_SIZE_X:
            continue

        for dz in range(-r, r + 1):
            z = pz + dz
            if z < 0 or z >= WORLD_SIZE_Z:
                continue

            for dy in range(-r, r + 1):
                y = py + dy - 3
                if y < 0 or y >= WORLD_SIZE_Y:
                    continue

                # Use r-squared (faster than sqrt(), remember?)
                if dx*dx + dy*dy + dz*dz <= r_squared:
                    block_type = world[x, y, z]
                    if block_type != AIR:
                        drawCube(x, y, z, block_type)


# ----- Hotbar Drawing -----
def drawHotbar():
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glDisable(GL_DEPTH_TEST)
    glDisable(GL_LIGHTING)

    hotbar_size = len(hotbar)
    slot_width = 60
    slot_height = 60
    padding = 3
    total_width = hotbar_size * (slot_width + padding) - padding
    start_x = (SCREEN_WIDTH - total_width) // 2
    y = 10

    glBegin(GL_QUADS)
    for i, block_type in enumerate(hotbar):
        x = start_x + i * (slot_width + padding)

        # Background slot
        glColor4f(0.3, 0.3, 0.3, 1)
        glVertex2f(x, y)
        glVertex2f(x + slot_width, y)
        glVertex2f(x + slot_width, y + slot_height)
        glVertex2f(x, y + slot_height)

        # Foreground icon (inner color)
        color = BLOCK_COLORS.get(block_type, (0, 0, 0, 0))
        glColor4fv(color)
        margin = 4
        glVertex2f(x + margin, y + margin)
        glVertex2f(x + slot_width - margin, y + margin)
        glVertex2f(x + slot_width - margin, y + slot_height - margin)
        glVertex2f(x + margin, y + slot_height - margin)
    glEnd()

    # Restore OpenGL state
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

# ----- Crosshair drawing -----
def drawCrosshair():
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0) # SCREEN_HEIGHT and the second 0 needs to be flipped like this if your y starting is on the top left
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_LIGHTING)

    cross_hair_width = 8
    cross_hair_height = 8
    start_x = SCREEN_WIDTH // 2
    start_y = SCREEN_HEIGHT // 2

    glColor4f(0.999, 0.999, 0.999, 1) # Pure white

    glBegin(GL_QUADS)
    glVertex2f(start_x, start_y)
    glVertex2f(start_x, start_y + 3)
    glVertex2f(start_x + 3, start_y + 3)
    glVertex2f(start_x + 3, start_y)
    glEnd()

    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)