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
    x=pos.x+i
    y=pos.y+i
    z=pos.z+i

    x2=x+10-(i*2)
    y2=y+0-(i*2)
    z2=z+10-(i*2)
    mc.setBlocks(x, y, z, x2, y2, z2, block)