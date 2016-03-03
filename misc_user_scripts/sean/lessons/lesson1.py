#Anything prefixed with this symbol is a comment, and ignored by the computer.
#Thus you can use it to explain what code does!

#Import the Python Minecraft library
import mcpi.minecraft as minecraft

#Create a connection to your local minecraft
mc = minecraft.Minecraft.create(address="162.244.165.151", name="seanybob") #NOTE - replace "seanybob" with your name

#Set the X/Y/Z coordinates of the person. Store coordinates in variables.
x = 10
y = 110
z = 12

#Using our connection to our local minecraft server...
#   For the player object...
#   Set the position to the x/y/z coordinates we just defined above.
mc.player.setPos(x, y, z)




#CHALLENGE 1
# Modify the script above to go to a different x/y/z location.

#CHALLENGE 2
# Figure out which of the three coordinates (x, y, or z) controls how high up you are in the air.