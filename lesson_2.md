# Lesson 2

#### Goal
Make a path of flowers spawn behind you while you walk. (Can replace flowers with any block id, such as lava)

#### New Concepts

```python
print "Hi!"
my_variable = 5
print my_variable
```

- The print command will print things to the terminal.
- This is useful for debugging, both to see when code got executed, and to see the contents of variables

-----------------

Now for a new construct, an infinite while loop!

Infinite while loops are used to make a set of code execute repeatedly, over and over, until the user decides to stop it.

An infinite while loop's structure looks like this:

```python
while True:
    <execute this indented code>
    <jump back to the top of the while statement>
```

For example, will constantly print the pattern "1 2 3 1 2 3 1 2 3 1 2 3..." over and over.

```python
while True:
    print "1"
    print "2"
    print "3"
```

In summary, an infinite while loop will keep executing the same code over and over until its it's forced to stop by the user by pressing control+c.

#### Code
Open up script.py in a code editor. Delete everything in it, we'll be starting from scratch!

```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob")
```
The first 2 lines are the same as they were in the previous lesson. Be sure to replace "seanybob" with your name!

-----------------

```python
import time
```
This line will import an additional python library we will be using called time - allowing us to "pause" the script for several seconds as needed.

-----------------

```python
print "Before loop."
```
This line just prints text to the terminal. We'll be using it as a method of debugging, so we can see when this line of code got executed.

-----------------

```python
while True:
```
Next, we open a while loop. Note that this loop's condition is simply 'True'. This means it will continue executing, forever, until you manually kill it with control+C. You can also close the terminal to kill it. This is also called an infinite loop.

-----------------

```python
    #Retrieve the current player's X, Y, and Z coordinates
    pos = mc.player.getPos()
```
Inside the while loop, the first thing we do is get the player's x/y/z coordinates. You'll note this is similar to the setPos function from lesson 1, though it's retrieving them instead of setting them!

IMPORTANT NOTE - you'll observe this line of code (and several lines underneath) are indented! This is how python tells which code belongs to the while loop, and needs to be executed in a loop. Indention is important in python!

-----------------

```python
    #Store the current player's coordinates in our variables x/y/z
    x = pos.x
    y = pos.y
    z = pos.z
```
Still inside the while loop, we store the player's position into x/y/z variables for later use.

-----------------

```python
    #This is the minecraft block ID of the flower block.
    block = 38
```
Still inside the while loop, we set Minecraft's block id for a flower to a variable called 'block' that we'll use later. You could put any block ID you want here. To see a list of block ids, check out [this website](http://minecraft-ids.grahamedgecombe.com/).

-----------------

```python
    #Set the block at the x/y/z coordinates of the current player to the block id we chose above.
    mc.setBlock(x, y, z, block)
```
Still inside the while loop, here we use our connection to the minecraft instance to set the block located at our x/y/z coordinates we stored earlier to the block id we stored earlier.

Since the x/y/z coordinates we stored earlier were our position, and the block id we stored earlier was a flower, what we are doing is putting a flower in the spot we are standing!

Moreover, since this is a loop, it means we should make a trail of flowers behind us while we walk! Let's finish this off so we can test it.

-----------------

```python
    #Wait for two tenths of a second, then jump back to the top of the while loop.
    print "LOOPING, waiting 0.2 seconds"
    time.sleep(0.2)
```
Still inside the while loop, here we print a statement letting us know the loop executed, then we tell the program to pause and wait for 0.2 seconds. This is important, because computers are lightning fast. If you don't do that pause, the computer will set the current block you are standing on to a flower thousands and thousands of times a second, and probably crash the minecraft server.

-----------------

```python
print "End of loop."
```
Finally the last line, which is OUTSIDE the while loop. We know that because it's not indented - that's how the computer knows the while loop has ended.


#### Terminal

Run the script like so:
```shell
python script.py
```

Note that it will run in an infinite loop. To end it you can hit control+C, or just close the terminal.


# CHALLENGES

- Modify the script above to put lava down instead of a flower ([block id explorer](http://minecraft-ids.grahamedgecombe.com/))
- Instead of putting the lava under the player, can you put it one block behind them (or to the side?)
- Try experimenting with a few other block IDs! Some ideas:
    - You could make a yellow brick road out of gold blocks.
    - You could lay minecraft track underneath where you walk, creating a roller coaster rapidly!
    
    
