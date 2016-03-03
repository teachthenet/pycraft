import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="162.244.165.151", name="seanybob") #NOTE - replace "seanybob" with your name

#The goal of this lesson is to create a building via code!
#   The setBlocks function takes as input the x/y/z coordinates of two opposite corners of a building.
#   For example, if you were to imagine looking at your house from the street,
#   the function would take as input the location of the bottom front right of your house AND the top back left.

# This position is the bottom front right of our building
x = 10
y = 110
z = 12

# This position is the top back left of our building.
# Note that we are defining it in relationship to the x/y/z (bottom right front) of our building
# That is to say, the top back left's x value is the bottom right front's x value + 10.
x2 = x + 10
y2 = y + 5
z2 = z + 8

#The result of the above should give us a building that is 10 blocks by 5 blocks by 8 blocks

#Let's build it now!

block = 4 
mc.setBlocks(x, y, z, x2, y2, z2, block)

# Pause here, and run it, and see what happens.

#CHALLENGE 1
# Modify the script above, and change the block used to build the building

#CHALLENGE 2
# Make the building twice as tall.

# You may notice something weird with challenge two. Which of the three variables (x, y, or z) ended up controlling the height?

#CHALLENGE 3
# Uncomment the code below and determine what it does. (To uncomment it, delete the hash sign # at the beginning of those two lines.)

#mystery_block_id = 0
#mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, mystery_block_id)

