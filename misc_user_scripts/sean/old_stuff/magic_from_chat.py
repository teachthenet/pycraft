import sys
sys.path.append("../../")
from mcpi import minecraft
import random
import time

server_address = "localhost"
rcon_port = 25575
rcon_password = "pycraft"
raspberry_juice_port = 4711
my_player_name = "seanybob"

import rcon_mc.rcon
import rcon_mc.lib.msocket

rcon=rcon_mc.rcon.client(server_address, rcon_port, rcon_password)
mc = minecraft.Minecraft.create(address="localhost", port=4711)

my_id = None
while not my_id:
    try:
        my_id = mc.getPlayerEntityId(my_player_name)
        print "Player", my_player_name, "found! Watching for spells..."
    except:
        print "Player", my_player_name, "not found."
        time.sleep(3)

active_spell = "spell:snowman"
valid_spells = ["spell:lightning", "spell:clear", "spell:teleport", "spell:explosive", "spell:water", "spell:lava", "spell:thor", "spell:snowman"]
while True:

    if active_spell == "spell:snowman":
        try:
            response=rcon.send("testfor @e[type=Arrow]")
            if "Found Arrow" in response:
                response=rcon.send("execute @e[type=Arrow] ~ ~ ~ summon SnowMan")
                response=rcon.send("kill @e[type=Arrow]")
        except:
            pass

    if active_spell == "spell:thor":
        try:
            response=rcon.send("testfor @e[type=Arrow]")
            if "Found Arrow" in response:
                response=rcon.send("execute @e[type=Arrow] ~ ~ ~ execute @e[r=50] ~ ~ ~ summon LightningBolt")
                response=rcon.send("kill @e[type=Arrow]")
        except:
            pass

    if active_spell == "spell:lava":
        try:
            response=rcon.send("testfor @e[type=Arrow]")
            if "Found Arrow" in response:
                response=rcon.send("execute @e[type=Arrow] ~ ~ ~ setblock ~ ~ ~ minecraft:flowing_lava")
                response=rcon.send("kill @e[type=Arrow]")
        except:
            pass

    if active_spell == "spell:water":
        try:
            response=rcon.send("testfor @e[type=Arrow]")
            if "Found Arrow" in response:
                response=rcon.send("execute @e[type=Arrow] ~ ~ ~ setblock ~ ~ ~ minecraft:flowing_water")
                response=rcon.send("kill @e[type=Arrow]")
        except:
            pass

    if active_spell == "spell:lightning":
        try:
            response=rcon.send("testfor @e[type=Arrow]")
            if "Found Arrow" in response:
                response=rcon.send("execute @e[type=Arrow] ~ ~ ~ summon LightningBolt")
                response=rcon.send("kill @e[type=Arrow]")
        except:
            pass

    if active_spell == "spell:explosive":
        try:
            response=rcon.send("testfor @e[type=Arrow]")
            if "Found Arrow" in response:
                response=rcon.send("execute @e[type=Arrow] ~ ~ ~ summon Creeper ~ ~ ~ {ignited:1,Fuse:1}")
                response=rcon.send("kill @e[type=Arrow]")
        except:
            pass

    if active_spell == "spell:teleport":
        try:
            response=rcon.send("testfor @e[type=Snowball]")
            if "Found Snowball" in response:
                response=rcon.send("tp seanybob @e[type=Snowball]")
                response=rcon.send("kill @e[type=Snowball]")
        except:
            pass
    
    for chatpost in mc.events.pollChatPosts():
        if chatpost.entityId == my_id:
            if chatpost.message in valid_spells:
                active_spell = chatpost.message

    time.sleep(.1)
    
    #response=rcon.send("execute @e[type=Arrow] ~ ~ ~ summon LightningBolt")
    #response=rcon.send("kill @e[type=Arrow]")
    #print response


"""
/execute @e[type=Arrow] ~ ~ ~ testforblock ~ ~-1 ~ ~

/testfor @e[type=Arrow,x=271,y=12,z=205]{inTile:3,inData:10b}

/testfor @e 271 12 205 [type=Arrow,InGround=3] {c=1}


/testfor @e[type=Arrow,x=271,y=12,z=205] {pickup:2b}

/testfor @e[type=Arrow,r=3] {inTile:minecraft:wool,inData:10b}


/execute @e[type=Arrow] ~ ~ ~ summon LightningBolt

/execute @e[type=Pig] ~ ~ ~ /tp @e[type=Pig,c=1] @e[type=Snowball,r=10]

execute @e[c=10] ~ ~ ~ execute @p ~ ~ ~ summon Creeper

/execute @p ~ ~ ~ /tp @p @e[type=Arrow,r=10]

"""


"""
Working tp to arrow
/give seanybob minecraft:command_block 1
/execute @p ~ ~ ~ /tp @p 271 12 205

/give seanybob minecraft:redstone_block 1
restoneblock = 152
commandblock = 137

/setblock 271 12 205 command_block 0 replace {Command:"testfor @p[_=1]"}

/setblock 271 90 205 command_block 0 replace {Command:"execute @p ~ ~ ~ /tp @p @e[type=Arrow,r=10]"}
"""