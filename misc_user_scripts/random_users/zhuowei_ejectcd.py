#!/usr/bin/env python

# mcpipy.com retrieved from URL below, written by zhuowei
# http://www.minecraftforum.net/topic/1639215-danfrisk-asks-for-physical-reality-does-opening-a-cdrom-from-minecraft-count/

import mcpi.minecraft as minecraft
import subprocess
import time
import server

#ip address of Pi

#ipAddr = "127.0.0.1"
mc = minecraft.Minecraft.create(server.address);

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        subprocess.call(["eject", "-T"])
    time.sleep(0.1)