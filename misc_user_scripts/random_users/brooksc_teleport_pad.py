#!/usr/bin/env python

# as shared on mcpipy.com

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import server


# If you are running this script with the bukkit mod, then use a diamond block as the magic center block for teleporting
# comment/uncomment below as appropriate
magic_block = block.DIAMOND_BLOCK # for bukkit server
#magic_block = block.NETHER_REACTOR_CORE # for raspberry pi

if __name__ == "__main__": # The script
    mc = minecraft.Minecraft.create(server.address)
    loc = mc.player.getPos()
    x = loc.x
    y = loc.y - 1
    z = loc.z
    for z_z in range (int(z-1), int(z+2)):
        for x_x in range(int(x-1), int(x+2)):
            mc.setBlock(x_x,y,z_z, block.COBBLESTONE)
            mc.setBlock(x_x,y+1,z_z, block.AIR)

mc.setBlock(x,y,z, magic_block)
