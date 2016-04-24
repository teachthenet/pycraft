# Lesson 2

#### Code Editor
Open up script.py in a code editor. Delete everything in it, we'll be starting from scratch!

```
import mcpi.minecraft as minecraft

#NOTE - replace "seanybob" below with your name
mc = minecraft.Minecraft.create(address="127.0.0.1", name="seanybob")
```
The first 3 lines are the same as they were in the previous lesson. Be sure to replace "seanybob" with your name!

-----------------

```
import time
```
This line will import an additional python library we will be using called time - allowing us to "pause" the script for several seconds as needed.

-----------------

```
print "Hi!"
my_variable = 5
print my_variable
```

- The print command will print things to the terminal.
- This is useful for debugging, both to see when code got executed, and to see the contents of variables

-----------------

Now for a new construct, a while loop!

A while loop has a format like so:

```
while <condition>:
    <execute this indented code>
    <jump back to the top of the while statement>
```

For example, this bit of code will print the numbers 1 to 10

```
my_counter = 1
while my_counter <= 10:
    print my_counter
    my_counter = my_counter + 1
```

- In this snippet, we start by creating a variable called 'my_counter' and setting it equal to 1.
- Then, we enter a while loop that continues executing until my_counter exceeds 10
- Inside the while loop, we keep printing the value stored in my_counter, and then incrementing that value by 1

In summary, a while loop will keep executing the same code over and over until its condition is no longer met, or until it's forced to stop by the user. A user can force code to stop that they are running in a terminal by hitting cmd+C (or control+c on a Windows machine).


-----------------

Now, for a big chunk of code. We're going to put the whole thing up here, then go through it line by line.

```
print "Before loop."

while True:

    #Retrieve the current player's X, Y, and Z coordinates
    pos = mc.player.getPos()

    #Store the current player's coordinates in our variables x/y/z
    x = pos.x
    y = pos.y
    z = pos.z

    #This is the minecraft block ID of the flower block.
    block = 38
    
    #Set the block at the x/y/z coordinates of the current player to the block id we chose above.
    mc.setBlock(x, y, z, block)
    
    #Wait for two tenths of a second, then jump back to the top of the while loop.
    print "LOOPING, waiting 0.2 seconds"
    time.sleep(0.2) 

print "End of loop."
```

To break it down line by line:

-----------------

```
print "Before loop."
```
This line just prints text to the terminal. We'll be using it as a method of debugging, so we can see when this line of code got executed.

-----------------

```
while True:
```
Next, we open a while loop. Note that this loop's condition is simply 'True'. This means it will continue executing, forever, until you manually kill it with cmd+C (or control+C). You can also close the terminal to kill it.

-----------------

```
    #Retrieve the current player's X, Y, and Z coordinates
    pos = mc.player.getPos()
```
Inside the while loop, the first thing we do is get the player's x/y/z coordinates. You'll note this is similar to the setPos function from lesson 1, though it's retrieving them instead of setting them!

IMPORTANT NOTE - you'll observe this line of code (and several lines underneath) are indented! This is how python tells which code belongs to the while loop, and needs to be executed in a loop. Indention is important in python!

-----------------

```
    #Store the current player's coordinates in our variables x/y/z
    x = pos.x
    y = pos.y
    z = pos.z
```
Still inside the while loop, we store the player's position into x/y/z variables for later use.

-----------------

```
    #This is the minecraft block ID of the flower block.
    block = 38
```
Still inside the while loop, we set Minecraft's block id for a flower to a variable called 'block' that we'll use later. You could put any block ID you want here. To see a list of block ids, check out [this website](http://minecraft-ids.grahamedgecombe.com/).

-----------------

```
    #Set the block at the x/y/z coordinates of the current player to the block id we chose above.
    mc.setBlock(x, y, z, block)
```
Still inside the while loop, here we use our connection to the minecraft instance to set the block located at our x/y/z coordinates we stored earlier to the block id we stored earlier.

Since the x/y/z coordinates we stored earlier were our position, and the block id we stored earlier was a flower, what we are doing is putting a flower in the spot we are standing!

Moreover, since this is a loop, it means we should make a trail of flowers behind us while we walk! Let's finish this off so we can test it.

-----------------

```
    #Wait for two tenths of a second, then jump back to the top of the while loop.
    print "LOOPING, waiting 0.2 seconds"
    time.sleep(0.2)
```
Still inside the while loop, here we print a statement letting us know the loop executed, then we tell the program to pause and wait for 0.2 seconds. This is important, because computers are lightning fast. If you don't do that pause, the computer will set the current block you are standing on to a flower thousands and thousands of times a second, and probably crash the minecraft server.

-----------------

```
print "End of loop."
```
Finally the last line, which is OUTSIDE the while loop. We know that because it's not indented - that's how the computer knows the while loop has ended.


#### Terminal

Run the script like so:
```
python script.py
```

Note that it will run in an infinite loop. To end it you can hit cmd+C (or control+C), or just close the terminal.


# CHALLENGES

- Modify the script above to put lava down instead of a flower.
- Instead of putting the lava under the player, can you put it one block behind them (or to the side?)
- Try experimenting with a few other block IDs! Some ideas:
    - You could make a yellow brick road out of gold blocks.
    - You could lay minecraft track underneath where you walk, creating a roller coaster rapidly!
    
    