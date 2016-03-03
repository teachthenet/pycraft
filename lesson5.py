import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="162.244.165.151", name="seanybob") #NOTE - replace "seanybob" with your name

#Using the concepts you learned in lesson4, make a pyramid.
#   _
#  ___
# _____
#_______

#Hint: Instead of thinking of the pyramid as one building,
#   think of every layer of the pyramid as a separate building that is only 1 block high.

#Here's some code to get you started. This creates the base of the pyramid.

block = 24

#Get the player's current position so we can build the pyramid there.
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

x2 = x + 8 #Make it 8 blocks wide.
y2 = y + 0 #Make it only one block high, so don't add anything here.
z2 = z + 8 #Make it 8 blocks long.

mc.setBlocks(x, y, z, x2, y2, z2, block)

# ...
# Continue the rest of the layers below. There should be 4 layers total (3 after the one completed above.)