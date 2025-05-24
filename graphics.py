#-----------------------------------------------------------------------------#
# This is the file that contains the definition for the graphics, like cubes,
# normals, drawing hotbar and etc.
#-----------------------------------------------------------------------------#

import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL
import math
import pygame

from blocks import *
from config import *
from inventory import *
from player import *

pygame.init()


# ------- Drawing a Cube -------
def draw_cube(z, y, x, block_type): # Draws a cube in the specified position
    if block_type == AIR:
        return None

    if not isBlockExposedToAir(z, y, x):
       return None

    # --- Vertices of the cube ---
    vertices_of_cube = np.array([
        [-0.5, -0.5,  0.5], [ 0.5, -0.5,  0.5], [ 0.5,  0.5,  0.5], [-0.5,  0.5,  0.5], # Front
        [-0.5, -0.5, -0.5], [-0.5,  0.5, -0.5], [ 0.5,  0.5, -0.5], [ 0.5, -0.5, -0.5], # Back
        [-0.5,  0.5,  0.5], [ 0.5,  0.5,  0.5], [ 0.5,  0.5, -0.5], [-0.5,  0.5, -0.5], # Top
        [-0.5, -0.5,  0.5], [-0.5, -0.5, -0.5], [ 0.5, -0.5, -0.5], [ 0.5, -0.5,  0.5], # Base
        [ 0.5, -0.5,  0.5], [ 0.5, -0.5, -0.5], [ 0.5,  0.5, -0.5], [ 0.5,  0.5,  0.5], # Right
        [-0.5, -0.5,  0.5], [-0.5,  0.5,  0.5], [-0.5,  0.5, -0.5], [-0.5, -0.5, -0.5]  # Left
    ])

    # --- Faces of the cube (Identification for each face) ---
    faces_of_cube = np.array([
        [0, 1, 2, 3], # Frente
        [4, 5, 6, 7], # Trás
        [8, 9, 10, 11], # Topo
        [12, 13, 14, 15], # Bases
        [16, 17, 18, 19], # Direita
        [20, 21, 22, 23]  # Esquerda
    ])

    # --- Normals fo the cube, for future lightning ---
    normals_of_cube = np.array([
        [ 0,  0,  1], [ 0,  0, -1], # Front, Back
        [ 0,  1,  0], [ 0, -1,  0], # Top, Base
        [ 1,  0,  0], [-1,  0,  0]  # Right, Left
    ])

    glPushMatrix() # Save the matrix of the current transformation
    glTranslatef(x + 0.5, y + 0.5, z + 0.5) # Move the cube to the world position

    color = BLOCK_COLORS.get(block_type, (1, 1, 1, 1))
    glColor4fv(color)

    glBegin(GL_QUADS)
    for i, face_indices in enumerate(faces_of_cube):
        # Checks visibility of cube
        nx, ny, nz = normals_of_cube[i]
        # Only draws the face if next block is AIR
        if getBlock(x + nx, y + ny, z + nz) == AIR:
            glNormal3fv(normals_of_cube[i]) # Normal for lightning
            for vertex_index in face_indices:
                glVertex3fv(vertices_of_cube[vertex_index])
    glEnd()

    glPopMatrix() # restore the transformation matrix


# --- World Drawing ---
def draw_world(): # Render based on sphere = More optimization
    
    px, py, pz = player_pos
    render_range = range(-render_distance, render_distance + 1)

    for dx in render_range:
        for dy in render_range:
            for dz in render_range:
                x = int(px + dx)
                y = int((py + dy) - 3)
                z = int(pz + dz)

                # Check world bounds
                if 0 <= x < WORLD_SIZE_X and 0 <= y < WORLD_SIZE_Y and 0 <= z < WORLD_SIZE_Z:
                    distance = math.sqrt(dx**2 + dy**2 + dz**2)
                    if distance <= render_distance:
                        block_type = world[x, y, z]
                        if block_type != AIR:
                            draw_cube(x, y, z, block_type)

# --- Hotbar Drawing ---
def draw_hotbar():
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_LIGHTING) # Disabling and after drawing enabling again, makes the hotbar normal color

    hotbar_size = len(hotbar)
    slot_width = 60
    slot_height = 60
    padding = 3
    total_width = hotbar_size * slot_width + (hotbar_size - 1) * padding
    total_height = hotbar_size * slot_height + (hotbar_size - 1) * padding
    start_x = (SCREEN_WIDTH - total_width) // 2
    start_y = total_height

    for i, block_type in enumerate(hotbar):
        x = start_x + i * (slot_width + padding)
        y = start_y


        glColor4f(0.3, 0.3, 0.3, 1) # Slot dark gray background
        
        glBegin(GL_QUADS)
        glVertex2f(x, y)
        glVertex2f(x + slot_width, y)
        glVertex2f(x + slot_width, y + slot_height)
        glVertex2f(x, y + slot_height)
        glEnd()

        # Draws block color (Simulating an icon)
        color_of_blocks = BLOCK_COLORS.get(block_type, (0, 0, 0, 0))
        glColor4fv(color_of_blocks)
        margin = 4
        glBegin(GL_QUADS)
        glVertex2f(x + margin, y + margin)
        glVertex2f(x + slot_width - margin, y + margin)
        glVertex2f(x + slot_width - margin, y + slot_height - margin)
        glVertex2f(x + margin, y + slot_height - margin)
        glEnd()

    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)

    # Restore matrix of projection/vision
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

# --- Crosshair drawing ---
def draw_crosshair():
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0) # SCREEN_HEIGHT and the second 0 needs to be flipped like this if your y starting is on the top left
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_LIGHTING)

    cross_hair_width = 6
    cross_hair_height = 6
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