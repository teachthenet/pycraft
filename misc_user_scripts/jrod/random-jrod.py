import sys
sys.path.append("../../")
from mcpi import minecraft
mc = minecraft.Minecraft.create()
import random


mc.postToChat("J-Rod test 2")
import time
while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    block = random.choice([10,11,12,13,14,15,16,17,18,19,20,21,22,23,79])
    mc.setBlock(x, y, z, block)
    time.sleep(0.2)