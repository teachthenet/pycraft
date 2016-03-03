# mcpipy.com retrieved from URL below, written by astrotutor
# http://www.minecraftforum.net/topic/1698103-camerasetpos-not-working-magic-trick/

import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

mc = minecraft.Minecraft.create()

# Find player position
playerPos = mc.player.getPos()

#Find block type below player
Block = mc.getBlock(playerPos.x, playerPos.y - 1, playerPos.z) 

# Set camera to above player position
mc.camera.setFollow()

# Build 1st wall across in front to right

length = 0
height = 0

while length < 5:

    mc.setBlock(playerPos.x + 2, playerPos.y + height, playerPos.z - 2 + length, 4)

    while height < 3:
        mc.setBlock(playerPos.x + 2, playerPos.y + height, playerPos.z - 2 + length, 4)
        time.sleep(0.2)
        height += 1

    length += 1
    height = 0

# Build second wall on right towards

length = 0
height = 0

while length < 4:
    mc.setBlock(playerPos.x + 1 - length, playerPos.y + height, playerPos.z + 2, 4)

    while height < 3:
        mc.setBlock(playerPos.x + 1 - length, playerPos.y + height, playerPos.z + 2, 4)
        time.sleep(0.2)
        height += 1

    length += 1
    height = 0

# Build third wall on left towards

length = 0
height = 0

while length < 4:
    mc.setBlock(playerPos.x + 1 - length, playerPos.y + height, playerPos.z - 2, 4)

    while height < 3:
        mc.setBlock(playerPos.x + 1 - length, playerPos.y + height, playerPos.z - 2 , 4)
        time.sleep(0.2)
        height += 1

    length += 1
    height = 0

# Build last wall behind to right

length = 0
height = 0

while length < 3:
    mc.setBlock(playerPos.x - 2, playerPos.y + height, playerPos.z - 1 + length, 4)

    while height < 3:
        mc.setBlock(playerPos.x - 2, playerPos.y + height, playerPos.z - 1 + length, 4)
        time.sleep(0.2)
        height += 1

    length += 1
    height = 0

# Build the roof

length = 1
width = 0

while length < 4:

    while width < 3:
        mc.setBlock(playerPos.x + 2 - length, playerPos.y + 2, playerPos.z - 1 + width, 5)
        time.sleep(0.2)
        width += 1

    length += 1
    width = 0

# Create void below house

length = 1
width = 0

while length < 4:

    while width < 3:
        mc.setBlock(playerPos.x + 2 - length, playerPos.y - 2, playerPos.z - 1 + width, 0)
        time.sleep(0.2)
        width += 1

    length += 1
    width = 0

length = 1
width = 0

while length < 4:

    while width < 3:
        mc.setBlock(playerPos.x + 2 - length, playerPos.y - 3, playerPos.z - 1 + width, 0)
        time.sleep(0.2)
        width += 1

    length += 1
    width = 0

# Remove the floor

length = 1
width = 0

while length < 4:

    while width < 3:
        mc.setBlock(playerPos.x + 2 - length, playerPos.y - 1, playerPos.z - 1 + width, 0)
        time.sleep(0.2)
        width += 1

    length += 1
    width = 0

# Build the floor



length = 1
width = 0

while length < 4:

    while width < 3:
        mc.setBlock(playerPos.x + 2 - length, playerPos.y - 1, playerPos.z - 1 + width, Block)
        time.sleep(0.2)
        width += 1

    length += 1
    width = 0

# Remove the roof

length = 1
width = 0

while length < 4:

    while width < 3:
        mc.setBlock(playerPos.x + 2 - length, playerPos.y + 2, playerPos.z - 1 + width, 0)
        time.sleep(0.2)
        width += 1

    length += 1
    width = 0

# Remove 1st wall across in front to right

length = 0
height = 0

while length < 5:

    mc.setBlock(playerPos.x + 2, playerPos.y + height, playerPos.z - 2 + length, 0)

    while height < 3:
        mc.setBlock(playerPos.x + 2, playerPos.y + height, playerPos.z - 2 + length, 0)
        time.sleep(0.2)
        height += 1

    length += 1
    height = 0

# Remove second wall on right towards

length = 0
height = 0

while length < 4:
    mc.setBlock(playerPos.x + 1 - length, playerPos.y + height, playerPos.z + 2, 0)

    while height < 3:
        mc.setBlock(playerPos.x + 1 - length, playerPos.y + height, playerPos.z + 2, 0)
        time.sleep(0.2)
        height += 1

    length += 1
    height = 0

# Remove third wall on left towards

length = 0
height = 0

while length < 4:
    mc.setBlock(playerPos.x + 1 - length, playerPos.y + height, playerPos.z - 2, 0)

    while height < 3:
        mc.setBlock(playerPos.x + 1 - length, playerPos.y + height, playerPos.z - 2 , 0)
        time.sleep(0.2)
        height += 1

    length += 1
    height = 0

# Remove last wall behind to right

length = 0
height = 0

while length < 3:
    mc.setBlock(playerPos.x - 2, playerPos.y + height, playerPos.z - 1 + length, 0)

    while height < 3:
        mc.setBlock(playerPos.x - 2, playerPos.y + height, playerPos.z - 1 + length, 0)
        time.sleep(0.2)
        height += 1

    length += 1
    height = 0 