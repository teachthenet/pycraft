#!/usr/bin/env python

# Quick rough & ready maze generator for Minecraft Pi edition.
# Dave Finch 2013

# mcpipy.com retrieved from URL below, written by davef21370
# https://github.com/brooksc/mcpipy/blob/master/davef21370_maze.py

import mcpi.minecraft as minecraft
import mcpi.block as block
import sys, random
from random import randint as rand
import server


# Connect to Minecraft.
try:
    mc = minecraft.Minecraft.create(server.address)
except:
    print "Cannot connect to Minecraft."
    sys.exit(0)

# Create a function for picking a random direction.
def randDir():
    r = rand(0,3)
    if r == 0: rv = (0,-1) # Up.
    if r == 1: rv = (0,1) # Down.
    if r == 2: rv = (-1,0) # Left.
    if r == 3: rv = (1,0) # Right.
    return rv

# Create a function to initialize the maze.
# w and h are the width and height respectively.
def initMaze(w,h):
    global maze,spl

    # Create a 2 dimensional array.
    maze = [[0]*h for x in range(w)]

    # Create four walls around the maze.
    # 1=wall, 0=walkway.
    for x in range(0,w):
        maze[x][0] = maze[x][h-1] = 1
        makeWall(ppos.x+x,ppos.z+0)
        makeWall(ppos.x+x,ppos.z+h-1)
    for y in range(0,mazeYSize):
        maze[0][y] = maze[w-1][y] = 1
        makeWall(ppos.x,ppos.z+y)
        makeWall(ppos.x+w-1,ppos.z+y)

    # Make every other cell a starting point.
    # 2=starting point.
    # Also create a list of these points to speed up the main loop.
    spl = []
    for y in range(2,h-2,2):
        for x in range(2,w-2,2):
            maze[x][y] = 2
            spl.append((x,y))
    # Shuffle the list of points and we can choose a random point by
    # simply "popping" it off the list.
    random.shuffle(spl)

def makeWall(x,z):
    mc.setBlock(x,ppos.y,z,block.STONE)
    mc.setBlock(x,ppos.y+1,z,block.STONE)
    mc.setBlock(x,ppos.y+2,z,block.STONE)

# Define the X and Y size of the maze including the outer walls.
# These values aren't checked but must be positive odd integers above 3.
mazeXSize = 35
mazeYSize = 35

# Set the maximum length of a wall.
maxWallLen = 1

# Find position of player and set base of maze 3 blocks lower.
ppos = mc.player.getPos()
ppos.y -= 3

# Clear an area for the maze.
for x in range(0,mazeXSize-1):
    for z in range(mazeYSize-1):
        mc.setBlock(ppos.x+x,ppos.y,ppos.z+z,block.STONE)
        for y in range(1,5):
            mc.setBlock(ppos.x+x,ppos.y+y,ppos.z+z,block.AIR)

# Create an empty maze.
initMaze(mazeXSize,mazeYSize)

# Loop until we have no more starting points (2's in the empty maze)
while filter(lambda x: 2 in x, maze):
    # Get the X and Y values of the first point in our randomized list.
    rx = spl[0][0]
    ry = spl[0][1]
    # Pop the first entry in the list, this deletes it and the rest move down.
    spl.pop(0)
    # Check to see if our chosen point is still a valid starting point.
    ud = False
    if maze[rx][ry] == 2:
        ud = True
        # Pick a random wall length up to the maximum.
        rc = rand(0,maxWallLen)
        # Pick a random direction.
        rd = randDir()
        fc = rd
        loop = True
        while loop:
            # Look in each direction, if the current wall being built is stuck inside itself start again.
            if maze[rx][ry-2] == 3 and maze[rx][ry+2] == 3 and maze[rx-2][ry] == 3 and maze[rx+2][ry] == 3:
                #
                # Code to clear maze area required
                #
                initMaze(mazeXSize,mazeYSize)
                break
            # Look ahead to see if we're okay to go in this direction.....
            cx = rx + (rd[0]*2)
            cy = ry + (rd[1]*2)
            nc = maze[cx][cy]
            if nc != 3:
                for i in range(0,2):
                    maze[rx][ry] = 3
                    makeWall(ppos.x+rx,ppos.z+ry)
                    rx += rd[0]
                    ry += rd[1]
            # .....if not choose another direction.
            else: rd = randDir()
            # If we hit an existing wall break out of the loop.
            if nc == 1: loop = False
            # Update our wall length counter. When this hits zero pick another direction.
            # This also makes sure the new direction isn't the same as the current one.
            rc -= 1
            if rc <= 0:
                rc = rand(0,maxWallLen)
                dd = rd
                de = (fc[0]*-1,fc[1]*-1)
                while dd == rd or rd == de:
                    rd = randDir()
    # The latest wall has been built so change all 3's (new wall) to 1's (existing wall)
    if ud:
        for x in range(0,mazeXSize):
            for y in range(0,mazeYSize):
                if maze[x][y] == 3: maze[x][y] = 1
    
