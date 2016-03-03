#!/usr/bin/env python

# mcpipy.com retrieved from URL below, written by jjinux
# http://jjinux.blogspot.com/2013/05/drawing-sierpinskis-triangle-in.html

"""Draw Sierpinski's triangle in Minecraft.

See: http://jjinux.blogspot.com/2013/05/drawing-sierpinskis-triangle-in.html

"""

import random

import mcpi.minecraft
import mcpi.block as block
import server

# It goes from -MAX_XZ to MAX_XZ.
MAX_XZ = 128
MAX_Y = 64

# These are the vertices of the triangle. It's a list of points. Each point
# is an (X, Y, X) tuple.
TRIANGLE_HEIGHT = MAX_Y - 1
TOP = (-MAX_XZ, TRIANGLE_HEIGHT, 0)
BOTTOM_LEFT = (MAX_XZ, TRIANGLE_HEIGHT, MAX_XZ)
BOTTOM_RIGHT = (MAX_XZ, TRIANGLE_HEIGHT, -MAX_XZ)
TRIANGLE_VERTICES = [TOP, BOTTOM_LEFT, BOTTOM_RIGHT]

BASE_BLOCK_ID = block.SANDSTONE.id
TRIANGLE_BLOCK_ID = block.SNOW.id

# This is the maximum number of iterations to let the algorithm run. The
# algorithm relies on randomness, so I'm just picking a sensible value.
MAX_ITERATIONS = MAX_XZ ** 2

PRINT_FREQ = 1000


def clear_board(minecraft):
    minecraft.setBlocks(-MAX_XZ, 0, -MAX_XZ, MAX_XZ, MAX_Y, MAX_XZ, 0)
    minecraft.setBlocks(-MAX_XZ, 0, -MAX_XZ, MAX_XZ, -MAX_Y, MAX_XZ, BASE_BLOCK_ID)


def draw_sierpinski_triangle(minecraft):

    def random_in_range():
        return random.randint(-MAX_XZ, MAX_XZ)

    def int_average(a, b):
        return int(round((a + b) / 2.0))

    # Draw the triangle vertices.

    for (x, y, z) in TRIANGLE_VERTICES:
        minecraft.setBlock(x, y, z, TRIANGLE_BLOCK_ID)

    # Pick a random point to start at.

    current = (random_in_range(),
               TRIANGLE_HEIGHT,
               random_in_range())

    for i in xrange(MAX_ITERATIONS):

        if i % PRINT_FREQ == 0:
            print("Drew %s blocks" % i)

        # Pick a random vertex to "walk" toward.

        destination = random.choice(TRIANGLE_VERTICES)

        # Draw a block in the middle of the current location and the
        # destination.

        (c_x, c_y, c_z) = current
        (d_x, d_y, d_z) = destination
        current = (
            int_average(c_x, d_x),
            TRIANGLE_HEIGHT,
            int_average(c_z, d_z)
        )
        (x, y, z) = current
        minecraft.setBlock(x, y, z, TRIANGLE_BLOCK_ID)


if __name__ == "__main__":
    minecraft = mcpi.minecraft.Minecraft.create(server.address)

    # Uncomment this if you need it.
    # clear_board(minecraft)
    
    draw_sierpinski_triangle(minecraft)