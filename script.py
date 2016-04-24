import mcpi.minecraft as minecraft

#NOTE - replace "seanybob" below with your name
mc = minecraft.Minecraft.create(address="127.0.0.1", name="seanybob") 

x = 10
y = 110
z = 12

mc.player.setPos(x, y, z)
