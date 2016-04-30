# Lesson 6

#### Goal
In this lesson, we're going to take the pyramid we created in lesson 5,
   and write an algorithm that will let us dynamically create it any size!
   To do this, look back at lesson 4, and see if you can detect a pattern in the numbers
   and how they change between each layer.

#### New Concepts

We have another new construct, a for loop!

For loops are used to repeat some code a set number of times.

A for loop looks similar to a while loop. Observe the example below, where we print the numbers 0 through 4.

```python
for i in range(5):
    print i
```

Note three things.

- First, you can change the number 5 to make it loop a different number of times.
- Second, the current # of the loop is saved in a variable called "i", which you can access in the loop - observe how we are printing that variable out!
- Third, note that it printed the numbers 0-4 (instead of 1-5)! This is because computers start counting from the number 0, instead of the number 1 like humans tend to. So by telling it you want a for loop with range(5), you are saying give me 5 iterations or numbers - which is 0 through 4!

#### Code
Open up script.py in a code editor. Delete everything in it, we'll be starting from scratch!

```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")
```
The first 2 lines are the same as the previous lesson. Be sure to replace "seanybob" with your name!

```python
block_id = 24
```
This is the block id for sandstone, which is good for a pyramid. Swap it to a different block ID if you'd like from [here](http://minecraft-ids.grahamedgecombe.com/).

```python
pos = mc.player.getPos()
```
Get the player's current position so we can build the pyramid there.



```python
for i in range(5):
    x = pos.x + i
    y = pos.y + i
    z = pos.z + i

    x2 = x + ?
    y2 = y
    z2 = z + ?
    mc.setBlocks(x, y, z, x2, y2, z2, block)
```
This is the foundation of your algorithm! We are going to create 5 layers in our pyramid, and thus loop through this code 5 times.

Note that the variable "i" will be replaced with the current iteration of our while loop (starting with 0 and going up to 4).

Note that the algorithm is not complete! Check the challenges below to see what you need to fix.

#### Terminal

Run the script like so:
```shell
python script.py
```

# CHALLENGES

- Did you notice a pattern in lesson 5? Make that pattern an algorithm above! Figure out what you need to replace the question marks with in the code supplied.

- Change the "5" in range(5) to a slightly larger number, like 10. CAREFUL! If you go too high, you'll crash the server! Keep it under 15 to be kind to your neighbors.

