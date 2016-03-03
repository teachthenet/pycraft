#!/usr/bin/env python

# mcpipy.com retrieved from URL below, written by burnaron
# http://www.minecraftforum.net/topic/1689199-my-first-script-bunkermaticpy/

import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *
import server

mc = minecraft.Minecraft.create(server.address)
x1 = -4
y1 = 3
z1 = 9
long_tun = 10
long_arc_ch = 8
long_ch = 26
long_m_ch = long_ch - 2 * long_arc_ch
deepness = 60
high_c_ch = 3

# FASE 1: cleaning zone
mc.setBlocks(x1-2,y1,z1-2,x1+2,y1+20,z1+2,0)
mc.setBlocks(x1-(long_tun+long_ch+1),y1-(deepness+1),z1-(long_tun+long_ch+1),x1+long_tun+long_ch+1,y1-(deepness-long_arc_ch-2-1),z1+long_tun+long_ch+1,1)

# FASE 2: establishing access
mc.setBlocks(x1-1.5,y1+2,z1-1.5,x1+1.5,y1-deepness,z1+1.5,1)
mc.setBlocks(x1-1,y1+2,z1-1,x1-1,y1-deepness,z1-1,0)

# FASE 3: establishing main tunnels, central chamber & and access stairs
# FASE 3.1: establishing central chamber
mc.setBlocks(x1-1,y1-deepness,z1-1,x1+1,y1-(deepness-high_c_ch),z1+1,0)

# FASE 3.2: establishing main tunnels
mc.setBlocks(x1-(long_tun+long_ch),y1-deepness,z1,x1+long_tun+long_ch,y1-(deepness-1),z1,0)
mc.setBlocks(x1,y1-deepness,z1-(long_tun+long_ch),x1,y1-(deepness-1),z1+long_tun+long_ch,0)

# FASE 3.3: establishing access stairs
mc.setBlocks(x1-1,y1+2,z1-1,x1-1,y1-deepness,z1-1,65,3)

# FASE 4: establishing main chambers
for pos in range(0,long_arc_ch):
    mc.setBlocks(x1+long_tun+pos,y1-deepness,z1-pos,x1+long_tun+pos,y1-(deepness-2)+pos,z1+pos,0)
    mc.setBlocks(x1-long_tun-pos,y1-deepness,z1-pos,x1-long_tun-pos,y1-(deepness-2)+pos,z1+pos,0)
    mc.setBlocks(x1-pos,y1-deepness,z1+long_tun+pos,x1+pos,y1-(deepness-2)+pos,z1+long_tun+pos,0)
    mc.setBlocks(x1-pos,y1-deepness,z1-long_tun-pos,x1+pos,y1-(deepness-2)+pos,z1-long_tun-pos,0)

mc.setBlocks(x1+long_tun+long_arc_ch,y1-deepness,z1-long_arc_ch,x1+long_tun+long_arc_ch+long_m_ch,y1-(deepness-2)+long_arc_ch,z1+long_arc_ch,0)
mc.setBlocks(x1-(long_tun+long_arc_ch),y1-deepness,z1-long_arc_ch,x1-(long_tun+long_arc_ch)-long_m_ch,y1-(deepness-2)+long_arc_ch,z1+long_arc_ch,0)
mc.setBlocks(x1-long_arc_ch,y1-deepness,z1+long_tun+long_arc_ch,x1+long_arc_ch,y1-(deepness-2)+long_arc_ch,z1+long_tun+long_arc_ch+long_m_ch,0)
mc.setBlocks(x1-long_arc_ch,y1-deepness,z1-(long_tun+long_arc_ch),x1+long_arc_ch,y1-(deepness-2)+long_arc_ch,z1-(long_tun+long_arc_ch)-(long_m_ch),0)

for pos in range(0,long_arc_ch):
    mc.setBlocks(x1+long_tun+long_arc_ch+long_m_ch+pos,y1-deepness,z1-long_arc_ch+pos,x1+long_tun+long_arc_ch+long_m_ch+pos,y1-(deepness-2)+long_arc_ch-pos,z1+long_arc_ch-pos,0)
    mc.setBlocks(x1-(long_tun+long_arc_ch)-long_m_ch-pos,y1-deepness,z1-long_arc_ch+pos,x1-(long_tun+long_arc_ch)-long_m_ch-pos,y1-(deepness-2)+long_arc_ch-pos,z1+long_arc_ch-pos,0)
    mc.setBlocks(x1-long_arc_ch+pos,y1-deepness,z1+long_tun+long_arc_ch+long_m_ch+pos,x1+long_arc_ch-pos,y1-(deepness-2)+long_arc_ch-pos,z1+long_tun+long_arc_ch+long_m_ch+pos,0)
    mc.setBlocks(x1-long_arc_ch+pos,y1-deepness,z1-(long_tun+long_arc_ch)-long_m_ch-pos,x1+long_arc_ch-pos,y1-(deepness-2)+long_arc_ch-pos,z1-(long_tun+long_arc_ch)-long_m_ch-pos,0)

# FASE 5: establishing lights & doors:
# FASE 5.1: central chamber lights:
mc.setBlock(x1,y1-(deepness-2),z1+1,50)
mc.setBlock(x1+1,y1-(deepness-2),z1,50)
mc.setBlock(x1,y1-(deepness-2),z1-1,50)
mc.setBlock(x1-1,y1-(deepness-2),z1,50)

# FASE 5.2: main chambers lights
for pos in range(2,long_arc_ch):
    mc.setBlock(x1+pos,y1-(deepness-2),z1+long_tun+pos,50)
    mc.setBlock(x1-pos,y1-(deepness-2),z1+long_tun+pos,50)
    mc.setBlock(x1+pos,y1-(deepness-2),z1-long_tun-pos,50)
    mc.setBlock(x1-pos,y1-(deepness-2),z1-long_tun-pos,50)
    mc.setBlock(x1+long_tun+pos,y1-(deepness-2),z1+pos,50)
    mc.setBlock(x1+long_tun+pos,y1-(deepness-2),z1-pos,50)
    mc.setBlock(x1-long_tun-pos,y1-(deepness-2),z1+pos,50)
    mc.setBlock(x1-long_tun-pos,y1-(deepness-2),z1-pos,50)

for pos in range(0,long_m_ch,2):
    mc.setBlock(x1+long_arc_ch,y1-(deepness-2),z1+long_tun+long_arc_ch+pos,50)
    mc.setBlock(x1-long_arc_ch,y1-(deepness-2),z1+long_tun+long_arc_ch+pos,50)
    mc.setBlock(x1+long_arc_ch,y1-(deepness-2),z1-(long_tun+long_arc_ch)-pos,50)
    mc.setBlock(x1-long_arc_ch,y1-(deepness-2),z1-(long_tun+long_arc_ch)-pos,50)
    mc.setBlock(x1+long_tun+long_arc_ch+pos,y1-(deepness-2),z1+long_arc_ch,50)
    mc.setBlock(x1+long_tun+long_arc_ch+pos,y1-(deepness-2),z1-long_arc_ch,50)
    mc.setBlock(x1-(long_tun+long_arc_ch)-pos,y1-(deepness-2),z1+long_arc_ch,50)
    mc.setBlock(x1-(long_tun+long_arc_ch)-pos,y1-(deepness-2),z1-long_arc_ch,50)

for pos in range(0,7):
    mc.setBlock(x1+long_arc_ch-pos,y1-(deepness-2),z1+long_tun+long_arc_ch+long_m_ch+pos,50)
    mc.setBlock(x1-long_arc_ch+pos,y1-(deepness-2),z1+long_tun+long_arc_ch+long_m_ch+pos,50)
    mc.setBlock(x1+long_arc_ch-pos,y1-(deepness-2),z1-(long_tun+long_arc_ch)-long_m_ch-pos,50)
    mc.setBlock(x1-long_arc_ch+pos,y1-(deepness-2),z1-(long_tun+long_arc_ch)-long_m_ch-pos,50)
    mc.setBlock(x1+long_tun+long_arc_ch+long_m_ch+pos,y1-(deepness-2),z1+long_arc_ch-pos,50)
    mc.setBlock(x1+long_tun+long_arc_ch+long_m_ch+pos,y1-(deepness-2),z1-long_arc_ch+pos,50)
    mc.setBlock(x1-(long_tun+long_arc_ch)-long_m_ch-pos,y1-(deepness-2),z1+long_arc_ch-pos,50)
    mc.setBlock(x1-(long_tun+long_arc_ch)-long_m_ch-pos,y1-(deepness-2),z1-long_arc_ch+pos,50)