#!/usr/bin/env python


# mcpipy.com retrieved from URL below, written by snowbound
# http://www.minecraftforum.net/topic/1680160-simple-flatmap-script/


import sys
import mcpi.minecraft as minecraft
import mcpi.block as block
import server


mc = minecraft.Minecraft.create(server.address)
mc.setBlocks(-128,0,-128,128,64,128,0)
if(len(sys.argv) > 1):
        bid = int(sys.argv[1])
else:
        bid = block.SANDSTONE.id

if bid < 0 or bid > 108:
        bid = block.SANDSTONE.id

mc.setBlocks(-128,0,-128,128,-64,128,bid)
