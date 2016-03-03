#!/usr/bin/env python

# mcpipy.com retrieved from URL below, written by burnaron
# http://www.minecraftforum.net/topic/1689199-my-first-script-bunkermaticpy/

import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *
import server

mc = minecraft.Minecraft.create(server.address)
x1 = 0
y1 = 0
z1 = 0
# FASE 1: cleaning zone
mc.setBlocks(x1-2,y1,z1-2,x1+2,y1+20,z1+2,0)
mc.setBlocks(x1-51,y1-61,z1-51,x1+51,y1-19,z1+51,1)
# FASE 2: establishing access
mc.setBlocks(x1-1.5,y1+2,z1-1.5,x1+1.5,y1-60,z1+1.5,1)
mc.setBlocks(x1-1,y1+2,z1-1,x1-1,y1-60,z1-1,0)
# FASE 3: establishing main tunnels
mc.setBlocks(x1-1,y1-60,z1-1,x1+1,y1-56,z1+1,0)
mc.setBlocks(x1-50,y1-60,z1,x1+50,y1-58,z1,0)
mc.setBlocks(x1,y1-60,z1-50,x1,y1-58,z1+50,0)
mc.setBlocks(x1-1,y1+2,z1-1,x1-1,y1-60,z1-1,65,3)
# FASE 4: establishing main chambers
for pos in range(0,8):
    mc.setBlocks(x1+10+pos,y1-60,z1-pos,x1+10+pos,y1-58+pos,z1+pos,0)
    mc.setBlocks(x1-10-pos,y1-60,z1-pos,x1-10-pos,y1-58+pos,z1+pos,0)
    mc.setBlocks(x1-pos,y1-60,z1+10+pos,x1+pos,y1-58+pos,z1+10+pos,0)
    mc.setBlocks(x1-pos,y1-60,z1-10-pos,x1+pos,y1-58+pos,z1-10-pos,0)

mc.setBlocks(x1+18,y1-60,z1-8,x1+18+24,y1-50,z1+8,0)
mc.setBlocks(x1-18,y1-60,z1-8,x1-18-24,y1-50,z1+8,0)
mc.setBlocks(x1-8,y1-60,z1+18,x1+8,y1-50,z1+18+24,0)
mc.setBlocks(x1-8,y1-60,z1-18,x1+8,y1-50,z1-18-24,0)

for pos in range(0,8):
    mc.setBlocks(x1+18+24+pos,y1-60,z1-8+pos,x1+18+24+pos,y1-50-pos,z1+8-pos,0)
    mc.setBlocks(x1-18-24-pos,y1-60,z1-8+pos,x1-18-24-pos,y1-50-pos,z1+8-pos,0)
    mc.setBlocks(x1-8+pos,y1-60,z1+18+24+pos,x1+8-pos,y1-50-pos,z1+18+24+pos,0)
    mc.setBlocks(x1-8+pos,y1-60,z1-18-24-pos,x1+8-pos,y1-50-pos,z1-18-24-pos,0)

# FASE 5: establishing lights & doors:
# FASE 5.1: central chamber lights:
mc.setBlock(0,-57,1,50)
mc.setBlock(1,-57,0,50)
mc.setBlock(0,-57,-1,50)
mc.setBlock(-1,-57,0,50)
# FASE 5.2: main chambers lights
for pos in range(2,8):
    mc.setBlock(x1+pos,y1-58,z1+10+pos,50)
    mc.setBlock(x1-pos,y1-58,z1+10+pos,50)
    mc.setBlock(x1+pos,y1-58,z1-10-pos,50)
    mc.setBlock(x1-pos,y1-58,z1-10-pos,50)
    mc.setBlock(x1+10+pos,y1-58,z1+pos,50)
    mc.setBlock(x1+10+pos,y1-58,z1-pos,50)
    mc.setBlock(x1-10-pos,y1-58,z1+pos,50)
    mc.setBlock(x1-10-pos,y1-58,z1-pos,50)

for pos in range(0,24,2):
    mc.setBlock(x1+8,y1-58,z1+18+pos,50)
    mc.setBlock(x1-8,y1-58,z1+18+pos,50)
    mc.setBlock(x1+8,y1-58,z1-18-pos,50)
    mc.setBlock(x1-8,y1-58,z1-18-pos,50)
    mc.setBlock(x1+18+pos,y1-58,z1+8,50)
    mc.setBlock(x1+18+pos,y1-58,z1-8,50)
    mc.setBlock(x1-18-pos,y1-58,z1+8,50)
    mc.setBlock(x1-18-pos,y1-58,z1-8,50)

for pos in range(0,7):
    mc.setBlock(x1+8-pos,y1-58,z1+18+24+pos,50)
    mc.setBlock(x1-8+pos,y1-58,z1+18+24+pos,50)
    mc.setBlock(x1+8-pos,y1-58,z1-18-24-pos,50)
    mc.setBlock(x1-8+pos,y1-58,z1-18-24-pos,50)
    mc.setBlock(x1+18+24+pos,y1-58,z1+8-pos,50)
    mc.setBlock(x1+18+24+pos,y1-58,z1-8+pos,50)
    mc.setBlock(x1-18-24-pos,y1-58,z1+8-pos,50)
    mc.setBlock(x1-18-24-pos,y1-58,z1-8+pos,50)
# FASE 5.3: doors
mc.setBlock(x1,y1-60,z1+2,64,1)
mc.setBlock(x1,y1-59,z1+2,64,8)
mc.setBlock(x1,y1-58,z1+2,1)
mc.setBlock(x1,y1-60,z1+10,64,3)
mc.setBlock(x1,y1-59,z1+10,64,8)
mc.setBlock(x1,y1-58,z1+10,1)

mc.setBlock(x1,y1-60,z1-2,64,3)
mc.setBlock(x1,y1-59,z1-2,64,8)
mc.setBlock(x1,y1-58,z1-2,1)
mc.setBlock(x1,y1-60,z1-10,64,1)
mc.setBlock(x1,y1-59,z1-10,64,8)
mc.setBlock(x1,y1-58,z1-10,1)

mc.setBlock(x1+2,y1-60,z1,64,4)
mc.setBlock(x1+2,y1-59,z1,64,8)
mc.setBlock(x1+2,y1-58,z1,1)
mc.setBlock(x1+10,y1-60,z1,64,2)
mc.setBlock(x1+10,y1-59,z1,64,8)
mc.setBlock(x1+10,y1-58,z1,1)
mc.setBlock(x1-2,y1-60,z1,64,2)
mc.setBlock(x1-2,y1-59,z1,64,8)
mc.setBlock(x1-2,y1-58,z1,1)
mc.setBlock(x1-10,y1-60,z1,64,4)
mc.setBlock(x1-10,y1-59,z1,64,8)
mc.setBlock(x1-10,y1-58,z1,1)