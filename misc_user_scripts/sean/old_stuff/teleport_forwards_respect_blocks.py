import sys
sys.path.append("../../")
from mcpi import minecraft

mc = minecraft.Minecraft.create(address = "localhost", port = 4711, name="seanybob")
import random
import time

while True:
    time.sleep(3)

    distance_to_travel = 10
    my_pos = mc.player.getPos()
    my_dir = mc.player.getDirection()

    for i in range(distance_to_travel):
        delta = {
            "x": my_dir.x*i,
            "y": my_dir.y*i+1,
            "z": my_dir.z*i,
        }
        block_found = mc.getBlock(my_pos.x+delta['x'], my_pos.y+delta['y'], my_pos.z+delta['z'])
        if block_found:
            distance_to_travel = i-1
            break

    delta = {
        "x": my_dir.x*distance_to_travel,
        "y": my_dir.y*distance_to_travel+1,
        "z": my_dir.z*distance_to_travel,
    }
    mc.player.setPos(my_pos.x+delta['x'], my_pos.y+delta['y'], my_pos.z+delta['z'])
