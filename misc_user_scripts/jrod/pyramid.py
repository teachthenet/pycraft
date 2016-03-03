import sys
sys.path.append("../../")
from mcpi import minecraft

mc = minecraft.Minecraft.create()
import random

mc.postToChat( ":]" )
block = 24
pos = mc.player.getPos()

#THIS IS THE BASE
x=pos.x
y=pos.y
z=pos.z

x2=x+8
y2=y+0
z2=z+8
mc.setBlocks(x, y, z, x2, y2, z2, block)

#THIS IS THE NEXT LEVEL
x=pos.x+1
y=pos.y+1
z=pos.z+1

x2=x+6
y2=y+0
z2=z+6
mc.setBlocks(x, y, z, x2, y2, z2, block)

# THIS IS THE LEVEL AFTER THE NEXT LEVEL
x=pos.x+2
y=pos.y+2
z=pos.z+2

x2=x+4
y2=y+0
z2=z+4
mc.setBlocks(x, y, z, x2, y2, z2, block)

# THIS IS THE LEVEL AFTER THE LEVEL AFTER THE NEXT LEVEL
x=pos.x+3
y=pos.y+3
z=pos.z+3

x2=x+2
y2=y+0
z2=z+2
mc.setBlocks(x, y, z, x2, y2, z2, block)