import sys
sys.path.append("../../")
from mcpi import minecraft

mc = minecraft.Minecraft.create(address="ngrok.com", port=37846)
import random

#Sandstone pyramid
mc.postToChat( "Dan Done" )
block = 46
pos = mc.player.getPos()

for i in range(5):
    x=pos.x+i
    y=pos.y+i
    z=pos.z+i
    
    x2=x+10-(i*2)
    y2=y+0-(i*2)
    z2=z+10-(i*2)
    mc.setBlocks(x, y, z, x2, y2, z2, block)
    
    
    
#air pyramid
    
#mc.postToChat( ":}" )
#air=0
#pos = mc.player.getPos()
#
#for i in range(10):
#    x=pos.x+i
#    y=pos.y+i-1
#    z=pos.z+i
#
#    x2=x+20-(i*2)
#    y2=y+0-(i*2)
#    z2=z+20-(i*2)
#    mc.setBlocks(x, y, z, x2, y2, z2, air)
#    mc.postToChat( "0-0" )
     
    
    
    
