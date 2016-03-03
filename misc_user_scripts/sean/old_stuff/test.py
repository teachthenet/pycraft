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

#mc = minecraft.Minecraft.create(address=server_address, port=raspberry_juice_port, name=my_player_name)

import rcon_mc.rcon
import rcon_mc.lib.msocket
client=rcon_mc.rcon.client(server_address, rcon_port, rcon_password)
while True:
    response=client.send("execute @e[type=Arrow] ~ ~ ~ summon LightningBolt")
    response=client.send("kill @e[type=Arrow]")
    print response
    time.sleep(1)

#my_pos = mc.player.getTilePos()
#print "my_pos", my_pos

#getBlockWithData
mc.setBlock(-131,28,-130, 137)
mc.getBlockWithData(-131,28,-130)
#mc.postToChat( "/execute @p ~ ~ ~ /tp @p @e[type=Arrow,r=300]{pickup:2b}" )


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