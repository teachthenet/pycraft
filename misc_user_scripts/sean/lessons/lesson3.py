import time
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="162.244.165.151", name="seanybob") #NOTE - replace "seanybob" with your name

#The goal of this lesson is to grant your character the ability to walk on water!
#   When a player is walking, if the block underneath them is water, we want to
#   automatically turn it into ice so they don't fall in!

water_block = 9
ice_block = 79

#Run this code continuously, until you cancel it in Terminal with cmd+C (control+c on windows/linux)
while True:

    #Retrieve the player's position
    pos = mc.player.getPos()

    #Save the player's position to x/y/z variables
    x = pos.x
    y = pos.y
    z = pos.z
    
    #Get the type of block below the player.
    #   To do this, subtract 1 block from the player's y position, to go one block below the player.
    block_below_player = mc.getBlock(x, y - 1, z)

    #This is a new construct, an if statement.
    #Similar to a while statement, it has a condition it checks, and then indented code underneath it.
    #For an if statement, that code is ONLY executed once if the condition is satisfied.
    #For a while statement, the code is continuously executed in a loop while the condition is satisfied.

    #Check and see, is the block below the player water?
    if block_below_player == water_block:
        #If it is water, turn it into ice.
        mc.setBlock(x, y - 1, z, ice_block)

    time.sleep(0.2)

# Pause here - run it and see what happens.


#CHALLENGE 1
# You may have noticed that the walk on water script isn't perfect, because there's
#   a slight delay before your script detects you are above water, and you sometimes fall in.
#   To fix that, instead of just checking the block underneath the player, modify the script to
#   also check the blocks directly underneath and in front, behind, and to the sides of the player.
#   This way, we can turn blocks into ice right before the player walks on them!

