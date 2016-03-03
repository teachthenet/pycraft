import sys
sys.path.append("../../")
from mcpi import minecraft

mc = minecraft.Minecraft.create(address="localhost", port=4711)
import random
import time
while True:    
    time.sleep(0.2)
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    blockBelow = mc.getBlock(x, y - 1, z)
    water = 9
    ice=79
    # if blockBelow == 2:
    mc.setBlock(1 + x, y + 1, z, 51)