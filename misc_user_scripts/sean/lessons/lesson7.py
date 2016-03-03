from mcpi import minecraft
import time

server_address = "162.244.165.151"
my_player_name = "seanybob"

mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)

#We first need to get our player ID, so we can focus on just listening to messages posted by us in chat
my_id = mc.getPlayerEntityId(my_player_name)

print "Script started! Type in 'hi' or 'testing' in minecraft chat to activate. Hit command (or control) + C in your terminal to stop."

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

            elif chatpost.message.lower() == "shield":
                mc.postToChat("Shield Activated")
                pos = mc.player.getPos(name="seanybob")
                mc.setBlocks(pos.x-1, pos.y-1, pos.z-1, pos.x+1, pos.y+2, pos.z+1, 20)
                mc.setBlocks(pos.x, pos.y, pos.z, pos.x, pos.y+1, pos.z, 0)

            elif chatpost.message.lower() == "nuke":
                mc.postToChat("INCOMING...")
                pos = mc.player.getPos()
                mc.setBlock(pos.x-6, pos.y, pos.z, 46) #TNT
                mc.setBlock(pos.x-6, pos.y-1, pos.z, 76) #Redstone Torch On

                mc.setBlock(pos.x+6, pos.y, pos.z, 46) #TNT
                mc.setBlock(pos.x+6, pos.y-1, pos.z, 76) #Redstone Torch On

                mc.setBlock(pos.x, pos.y, pos.z+6, 46) #TNT
                mc.setBlock(pos.x, pos.y-1, pos.z+6, 76) #Redstone Torch On

                mc.setBlock(pos.x, pos.y, pos.z-6, 46) #TNT
                mc.setBlock(pos.x, pos.y-1, pos.z-6, 76) #Redstone Torch On

            elif chatpost.message.lower().split(' ')[0] == "jail":
                opponent_name = chatpost.message.lower().split(' ')[1]
                mc.postToChat("Jailed "+opponent_name)
                opponent_mc = minecraft.Minecraft.create(address=server_address, name=opponent_name)
                o_pos = opponent_mc.player.getPos()
                mc.setBlocks(o_pos.x-1, o_pos.y-1, o_pos.z-1, o_pos.x+1, o_pos.y+2, o_pos.z+1, 7)
                mc.setBlocks(o_pos.x, o_pos.y, o_pos.z, o_pos.x, o_pos.y+1, o_pos.z, 0)

    time.sleep(.1)


#CHALLENGE 1
# Modify the script above, and add a chat trigger called "shield" that builds a glass shield "building"
#   all around you, making it so nothing can attack you but you can still see. Hint: Refer to lesson5

#CHALLENGE 2
# Modify the script above, and add a chat trigger called "nuke" that spawns several TNT around you.
#   You'll also need to spawn redstone torches next to the TNT to activate it. (Try under)
#   Make sure you spawn the TNT far enough away from you it doesn't kill you, but close enough it can
#   take out your enemies!
