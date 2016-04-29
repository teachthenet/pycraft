# Lesson 5

#### Goal
Using the concepts you learned in lesson4, make a pyramid programmatically.
```
   _
  ___
 _____
_______
```

Hint: Instead of thinking of the pyramid as one building, think of every layer of the pyramid as a separate building that is only 1 block high.

#### New Concepts

- Copying and Pasting is one of the most important tools for a developer!
- If you are writing similar code repeatedly, consider copying and pasting it, then editing the resulting code.
- The shortcut for copying is cmd+C on a mac, or control+C on a windows machine.
- The shortcut for pasting is cmd+V on a mac, or control+V on a windows machine.

#### Code
Open up script.py in a code editor. Delete everything in it, we'll be starting from scratch!

```
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")
```
The first 2 lines are the same as the previous lesson. Be sure to replace "seanybob" with your name!

```
block_id = 24
```
This is the block id for sandstone, which is good for a pyramid. Swap it to a different block ID if you'd like from [here](http://minecraft-ids.grahamedgecombe.com/).

```
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
```
Get the player's current position so we can build the pyramid there.



```
x2 = x + 8 #Make it 8 blocks wide.
y2 = y + 0 #Make it only one block high, so don't add anything here.
z2 = z + 8 #Make it 8 blocks long.

mc.setBlocks(x, y, z, x2, y2, z2, block_id)
```

Craft the bottom layer of the pyramid. This is the chunk of code you will need to copy and paste to create the additional layers. Create 3 more layers after this one to complete the pyramid on your own.

#### Terminal

Run the script like so:
```
python script.py
```

# CHALLENGES

- Complete the remaining 3 layers of the pyramid (missing from the code above)

