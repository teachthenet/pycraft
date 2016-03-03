#!/usr/bin/env python

#www.stuffaboutcode.com
#Raspberry Pi, Minecraft - auto bridge

# mcpipy.com retrieved from URL below, written by stuffaboutcode
# http://www.stuffaboutcode.com/2013/02/raspberry-pi-minecraft-auto-bridge.html

#import the minecraft.py module from the minecraft directory
import mcpi.minecraft as minecraft
#import minecraft block module
import mcpi.block as block
#import time, so delays can be used
import time
import server


#function to round players float position to integer position
def roundVec3(vec3):
    return minecraft.Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

if __name__ == "__main__":

    time.sleep(2)

    #Connect to minecraft by creating the minecraft object
    # - minecraft needs to be running and in a game
    mc = minecraft.Minecraft.create(server.address)

    #Post a message to the minecraft chat window
    mc.postToChat("Hi, Minecraft - Auto Bridge Active")
    mc.postToChat("www.stuffaboutcode.com")

    #Get the players position
    lastPlayerPos = mc.player.getPos()

    while (True):

        #Get the players position
        playerPos = mc.player.getPos()

        #Find the difference between the player's position and the last position
        movementX = lastPlayerPos.x - playerPos.x
        movementZ = lastPlayerPos.z - playerPos.z

        #Has the player moved more than 0.2 in any horizontal (x,z) direction

        if ((movementX < -0.2) or (movementX > 0.2) or (movementZ < -0.2) or (movementZ > 0.2)):

            #Project players direction forward to the next square
            nextPlayerPos = playerPos
            # keep adding the movement to the players location till the next block is found
            while ((int(playerPos.x) == int(nextPlayerPos.x)) and (int(playerPos.z) == int(nextPlayerPos.z))):
                nextPlayerPos = minecraft.Vec3(nextPlayerPos.x - movementX, nextPlayerPos.y, nextPlayerPos.z - movementZ)

            #Is the block below the next player pos air, if so fill it in with DIAMOND
            blockBelowPos = roundVec3(nextPlayerPos)
            blockBelowPos.z = blockBelowPos.z - 1
            blockBelowPos.y = blockBelowPos.y - 1
            if mc.getBlock(blockBelowPos) == block.AIR:
                mc.setBlock(blockBelowPos.x, blockBelowPos.y, blockBelowPos.z, block.DIAMOND_BLOCK)

            #Store players last position
            lastPlayerPos = playerPos

            #Delay
        time.sleep(0.01)