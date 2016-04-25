# Lesson 4

#### Goal
Create a building programmatically

#### New Concepts

Variables can refer to each other, similar to algebra
```
x = 10
x2 = x + 5
```
x2 now is 15

```
mc.setBlocks(x, y, z, x2, y2, z2, block_id)
```

- There is a new function we can use called setBlocks.
- The setBlocks function takes as input the x/y/z coordinates of two opposite corners of a building.
- For example, if you were to imagine looking at your house from the street, the function would take as input the location of the bottom front right of your house AND the top back left.
- The function then sets every block inside the cuboid you defined as the block_id you passed in

#### Code
Open up script.py in a code editor. Delete everything in it, we'll be starting from scratch!

```
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="127.0.0.1", name="seanybob")
```
The first 2 lines are similar to the previous lesson. Be sure to replace "seanybob" with your name!

```
x = 10
y = 110
z = 12
```

This position is the bottom front right of our building

```
x2 = x + 10
y2 = y + 5
z2 = z + 8
```

- This position is the top back left of our building.
- Note that we are defining it in relationship to the x/y/z (bottom right front) of our building
- That is to say, the top back left's x value is the bottom right front's x value + 10.

```
block_id = 4
```
This is the block id for cobbestone. Swap it to a different block ID if you'd like from [here](http://minecraft-ids.grahamedgecombe.com/).

```
mc.setBlocks(x, y, z, x2, y2, z2, block_id)
```
The result of the above should give us a building that is 10 blocks by 5 blocks by 8 blocks

#### Terminal

Run the script like so:
```
python script.py
```

# CHALLENGES

- Modify the script above, and change the block used to build the building
- Make the building twice as tall.
- Add the code below and determine what it does.
```
mystery_block_id = 0
mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, mystery_block_id)
```

