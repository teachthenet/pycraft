import mcpi.minecraft as minecraft

#NOTE - replace "seanybob" below with your name
mc = minecraft.Minecraft.create(address="127.0.0.1", name="seanybob") 

x = 10
y = 110
z = 12

mc.player.setPos(x, y, z)




#CHALLENGE 1
# Modify the script above to go to a different x/y/z location.

#CHALLENGE 2
# Figure out which of the three coordinates (x, y, or z) controls how high up you are in the air.