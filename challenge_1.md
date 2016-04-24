# CHALLENGE 1

Open up script.py in a code editor. We'll be going through this file line-by-line to start with.

```
import mcpi.minecraft as minecraft
```
This first line imports the mcpi.minecraft library, making it available under the name 'minecraft'

-----------------

```
#NOTE - replace "seanybob" below with your name
mc = minecraft.Minecraft.create(address="127.0.0.1", name="seanybob")
```

- Anything prefixed by the '#' symbol is a comment for humans, and is ignored by the computer.
- Here we see we are creating a connection to the minecraft server and storing it in a variable named "mc".
- The server we are connecting to is located at IP address 127.0.0.1 and linking to the login name "seanybob".
- As mentioned in the comment above it, you need to change "seanybob" to your minecraft name that you chose.

-----------------

```
x = 10
y = 110
z = 12
```

- Here we are creating 3 variables for later use.
- In the variable named 'x', we are storing the number 10.

-----------------

```
mc.player.setPos(x, y, z)
```

- Using our connection to our minecraft server (we previously saved the connection to the mc variable)...
- We will access our player object inside that minecraft server...
- And then set our position in the minecraft server to the x/y/z coordinates indicated by the variables we just set earlier.

The variables in the call get replaced, essentially turning into the values we stored in them earlier:
```
mc.player.setPos(10, 110, 12)
```

To execute the script, in your terminal cd to the directory the script is located:
```
cd ~/TeachCraft-Challenges
```

Then run the script like so:
```
python script.py
```

----------------------

# CHALLENGES

- Modify the script to go to a different x/y/z location.
- Figure out which of the three coordinates (x, y, or z) controls how high up you are in the air.
