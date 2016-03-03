import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="162.244.165.151", name="seanybob") #NOTE - replace "seanybob" with your name

#In this lesson, we're going to take the pyramid we created in lesson 5,
#   and write an algorithm that will let us dynamically create it any size!
#   To do this, look back at lesson 4, and see if you can detect a pattern in the numbers
#   and how they change between each layer.

#STOP HERE.

#Connect with a dev and we'll walk you through how to create and manipulate the algorithm shown below.

block = 46
pos = mc.player.getPos()

for i in range(5):
    x = pos.x + i
    y = pos.y + i
    z = pos.z + i

    x2 = x + ?
    y2 = y + ?
    z2 = z + ?
    mc.setBlocks(x, y, z, x2, y2, z2, block)

# CHALLENGE 1: Did you notice a pattern in lesson 5? Make that pattern an algorithm above!
# Figure out what you need to replace the question marks with above.

# CHALLENGE 2: Ok, we gotta do it once. Change the "5" in range(5) to a slightly larger number, like 10.
#   CAREFUL! If you go too high, you'll crash the server!