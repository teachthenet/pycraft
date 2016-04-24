# Lesson 3

#### Goal
Grant your character the ability to walk on water (by turning water blocks underneath the player into ice blocks)

#### New Concept
If statements are a way of checking a condition, similar to a while loop. Instead of looping though, they only execute once, and only if their condition is met.
```
if <condition>:
    <execute this code>
```

```
x = 4
if x == 3:
    print "x is 3"
```
This only runs the print statement if x is 3. Note the double equals sign in the if statement! It's super important. Double equals checks if something is equivalent, while a single equals actually assigns something.


```
if y > 10:
    if x > 10:
        print "y is at least 10 blocks high and x is at least 10 blocks distant"
```
Note that you can stack if statements, so long as you stack the indentation.

```
if y >= 10 and y <= 20:
    print "y between 10 and 20 blocks high"
```
You can also combine if statements using "and" / "or" operators.


#### Code
Open up script.py in a code editor. Delete everything in it, we'll be starting from scratch!

```
import mcpi.minecraft as minecraft

#NOTE - replace "seanybob" below with your name
mc = minecraft.Minecraft.create(address="127.0.0.1", name="seanybob")

import time
```
The first 4 lines are the same as they were in the previous lesson. Be sure to replace "seanybob" with your name!

```
water_block = 9
ice_block = 79
```

Next we store the block IDs for water and ice in variables for us to use later.

```
while True:
```

Next we want an eternal loop that keeps running our next chunk of code until we tell it to stop.

```
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
```
Inside the while loop, we want to get the player's current position, and stick it in variables for us to refer to later.

```
    block_below_player = mc.getBlock(x, y - 1, z)
```
Inside the while loop, we want to get the block beneath the player. To do this, we execute the getBlock function, passing it the x/y/z coordinate right below the player! Note the y-1. Since the player's location is x/y/z, by subtracting 1 from y we get the block immediately underneath the player.

```
    #This is a new construct, an if statement.
    #Similar to a while statement, it has a condition it checks, and then indented code underneath it.
    #For an if statement, that code is ONLY executed once if the condition is satisfied.
    #For a while statement, the code is continuously executed in a loop while the condition is satisfied.

    #Check and see, is the block below the player water?
    if block_below_player == water_block:
        #If it is water, turn it into ice.
        mc.setBlock(x, y - 1, z, ice_block)

    time.sleep(0.2)
```

# Pause here - run it and see what happens.


#CHALLENGE 1
# You may have noticed that the walk on water script isn't perfect, because there's
#   a slight delay before your script detects you are above water, and you sometimes fall in.
#   To fix that, instead of just checking the block underneath the player, modify the script to
#   also check the blocks directly underneath and in front, behind, and to the sides of the player.
#   This way, we can turn blocks into ice right before the player walks on them!

