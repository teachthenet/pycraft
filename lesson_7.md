# Lesson 7

#### Goal

In this lesson, we'll be setting up a magic system! We'll create a listener that waits for us to type a spell into minecraft chat, and once a spell is typed, the script executes the python code corresponding to that spell!

#### New Concepts

In this lesson, we'll look at another for loop!

```
for chatpost in mc.events.pollChatPosts():
    print chatpost
```

This code will execute the code inside the while loop once for every chat message found in the minecraft chat post since the last time we looked. By sticking this in an infinite while loop, we can actually watch all messages posted in chat, forever!


#### Code
Open up script.py in a code editor. Delete everything in it, we'll be starting from scratch!

```
from mcpi import minecraft
import time

server_address = "199.96.85.3"
my_player_name = "seanybob"

mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)
```
These first few lines are similar to the previous lesson. Be sure to replace "seanybob" with your name!

```
my_id = mc.getPlayerEntityId(my_player_name)
```
We first need to get our player ID, so we can focus on just listening to messages posted by us in chat

```
print "Script started! Type in 'hi' or 'testing' in minecraft chat to activate. Hit command (or control) + C in your terminal to stop."
```
Let's add a print message to tell us when the script started.

```
#Watch for chat messages
while True:

    #For each chat message since the last time we checked...
    for chatpost in mc.events.pollChatPosts():

        #Was the chat message sent by me?
        if chatpost.entityId == my_id:

            #if so, let's do something!
            if chatpost.message.lower() == "hi":
                mc.postToChat("Hello right back at you!")

            elif chatpost.message.lower() == "testing":
                mc.postToChat("123")

    time.sleep(.1)
```
This is the foundation of our script! In an infinite while loop, we listen for chatposts. Whenever a chatpost is detected, we check if it was sent by us. If so, we check the contents of the message. If it matches one of the messages we are looking for, we execute python code!

#### Terminal

Run the script like so:
```
python script.py
```

# CHALLENGE 1
 Modify the script above, and add a chat trigger called "shield" that builds a glass shield "building"
   all around you, making it so nothing can attack you but you can still see. Hint: Refer to lesson5

# CHALLENGE 2
 Modify the script above, and add a chat trigger called "nuke" that spawns several TNT around you.
   You'll also need to spawn redstone torches next to the TNT to activate it. (Try under)
   Make sure you spawn the TNT far enough away from you it doesn't kill you, but close enough it can
   take out your enemies!

# CHALLENGE 3
 Modify the script above, and add a chat trigger called "jail" that puts your opponent into a bedrock prison.
   This is similar to the "shield" spell, with a few differences.
   1) Instead of using glass, use bedrock.
   2) Instead of centering it around YOUR position, you need to center it around your OPPONENT's position!
   3) Instead of a single trigger word, you need two. E.g. instead of just "shield" you need "jail seanybob"

   When thinking about how to approach this, think of the flow of data. You're passing in your opponent's
   name via a parameter, so you'll need to extract that. Now, you have your opponent's name, but the getPos()
   function doesn't have a name parameter! Try thinking back to what you did earlier in the script to create
   a connection to the minecraft server for a specific name.