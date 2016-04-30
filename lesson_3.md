# Lesson 3

#### Goal
Grant your character the ability to walk on water (by turning water blocks underneath the player into ice blocks)

#### New Concepts

```python
if <condition>:
    <execute this code>
```

- We have another construct called an if statement.
- An If statement has a condition it checks.
- If the condition passes (is true), it executes the indented code underneath it ONCE.
- If the condition fails (it is not true), it skips the indented code underneath it.
- So an IF statement executes its code once, while a While loop executes it repeatedly!

```python
x = 4
if x == 3:
    print "x is 3"
```

This only runs the print statement if x is 3. Note the double equals sign in the if statement! It's super important. Double equals checks if something is equivalent (compared to a single equals which assigns something to a variable).

```python
if y > 10:
    if x > 10:
        print "y is at least 10 blocks high and x is at least 10 blocks distant"
```

Note that you can stack if statements, so long as you stack the indentation.

```python
if y >= 10 and y <= 20:
    print "y between 10 and 20 blocks high"
```

You can also combine if statements using "and" / "or" operators.


#### Code
Open up script.py in a code editor. Delete everything in it, we'll be starting from scratch!

```python
import time
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")
```
The first 3 lines are the same as they were in the previous lesson. Be sure to replace "seanybob" with your name!

```python
water_block = 9
ice_block = 79
```

Next we store the block IDs for water and ice in variables for us to use later.

```python
while True:
```

Next we want an infinite loop that keeps running our next chunk of code until we tell it to stop.

```python
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
```
Inside the while loop, we want to get the player's current position, and stick it in variables for us to refer to later.

```python
    block_below_player = mc.getBlock(x, y - 1, z)
```
Inside the while loop, we want to get the block beneath the player. To do this, we execute the getBlock function, passing it the x/y/z coordinate right below the player! Note the y-1. Since the player's location is x/y/z, by subtracting 1 from y we get the block immediately underneath the player.

```python
    #If the block below the player is water, turn it into ice.
    if block_below_player == water_block:
        mc.setBlock(x, y - 1, z, ice_block)
```
Inside the while loop, Check and see if the block underneath the player is water. If so, turn it into ice!

```python
    time.sleep(0.2)
```
Inside the while loop, Pause for 0.2 seconds


#### Terminal

Run the script like so:
```shell
python script.py
```

Note that it will run in an infinite loop. To end it you can hit cmd+C (or control+C), or just close the terminal.


# CHALLENGES

You may have noticed that the walk on water script isn't perfect, because there's a slight delay before your script detects you are above water, and you sometimes fall in.

To fix that, instead of just checking the block underneath the player, modify the script to also check the blocks directly underneath and in front, behind, and to the sides of the player.

This way, we can turn blocks into ice right before the player walks on them!

    
