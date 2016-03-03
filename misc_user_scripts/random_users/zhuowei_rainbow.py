#!/usr/bin/env python

#
# mcpipy.com retrieved from URL below, written by zhuowei
# http://www.minecraftforum.net/topic/1638036-my-first-script-for-minecraft-pi-api-a-rainbow/

import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *
import server

colors = [14, 1, 4, 5, 3, 11, 10]

mc = minecraft.Minecraft.create(server.address)
height = 60

mc.setBlocks(-64,0,0,64,height + len(colors),0,0)
for x in range(0, 128):
        for colourindex in range(0, len(colors)):
                y = sin((x / 128.0) * pi) * height + colourindex
                mc.setBlock(x - 64, int(y), 0, block.WOOL.id, colors[len(colors) - 1 - colourindex])