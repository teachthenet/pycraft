#Anything prefixed with this symbol is a comment, and ignored by the computer.
#Thus you can use it to explain what code does!

#Imports
import mcpi.minecraft as minecraft
import time 

#Create a connection to minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob") #NOTE - replace "seanybob" with your name
#address="topopps.mcph.co"

#This is a new construct to learn!
#   A while statement has the format like so:
#   while <condition>:
#       <execute this indented code>
#       <jump back to the top of the while statement>
#
#   This means that the while statement acts as a loop, executing the same code
#   over and over until it's condition is no longer met.
#
#   In this case, since the condition is simply "True", it will always run, forever, without stopping!
#   That means you'll have to manually stop it. To stop it, go to the terminal you ran it in, and hit cmd+C (control+c on windows)

print "Before loop."

while True:

    #Retrieve the current player's X, Y, and Z coordinates
    pos = mc.player.getPos()

    #Store the current player's coordinates in our variables x/y/z
    x = pos.x
    y = pos.y
    z = pos.z

    #This is the minecraft block ID of the flower block.
    #To see what other block IDs are available, go here in your browser: http://minecraft-ids.grahamedgecombe.com/
    block = 38
    
    #Set the block at the x/y/z coordinates of the current player to the block id we chose above.
    mc.setBlock(x, y, z, block)
    
    #Wait for two tenths of a second, then jump back to the top of the while loop.
    print "LOOPING, waiting 0.2 seconds"
    time.sleep(0.2) 

print "End of loop."


#CHALLENGE 1
# Modify the script above to put lava down instead of a flower.

#CHALLENGE 2
# Instead of putting the lava under the player, can you put it one block behind them (or to the side?)

#CHALLENGE 3
# Try experimenting with a few other block IDs! Some ideas:
#   - You could make a yellow brick road out of gold blocks.
#   - You could lay minecraft track underneath where you walk, creating a roller coaster rapidly!