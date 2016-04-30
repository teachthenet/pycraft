from mcpi import minecraft
import rcon_mc.rcon
import rcon_mc.lib.msocket

server_address = "199.96.85.3"
rcon_port = 25575
rcon_password = "pycraft"
raspberry_juice_port = 4711
my_player_name = "seanybob"

mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)
rcon = rcon_mc.rcon.client(server_address, rcon_port, rcon_password)

rcon.send('scoreboard objectives add ID dummy')

#Grant player bows to trigger spells

#Spell:Snowman
rcon.send('give '+my_player_name+' minecraft:bow 1 0 {display:{Name:"Spell:Snowman",Lore:["Summon a snowman."]},ench:[{id:51,lvl:1},{id:34,lvl:100},{id:48,lvl:1}]}')

#Spell:Explosion
rcon.send('give '+my_player_name+' minecraft:bow 1 0 {display:{Name:"Spell:Explosion",Lore:["Create an explosion."]},ench:[{id:51,lvl:1},{id:34,lvl:100},{id:48,lvl:2}]}')

#Spell:Teleport
rcon.send('give '+my_player_name+' minecraft:bow 1 0 {display:{Name:"Spell:Teleport",Lore:["Teleport to target location."]},ench:[{id:51,lvl:1},{id:34,lvl:100},{id:48,lvl:3}]}')

#Give player arrows to use with the bow
rcon.send('give '+my_player_name+' minecraft:arrow 1 0')

#Watch for spellcasts
while True:

    try:

        #Any arrows fired from the Snowman bow?
        rcon.send('scoreboard players set @e[type=Arrow] ID 1 {damage:3.0}') #Power 1 Enchantment
        response = rcon.send("execute @e[type=Arrow,score_ID_min=1,score_ID=1] ~ ~ ~ summon SnowMan")


        #Any arrows fired from the Explosion bow?
        rcon.send('scoreboard players set @e[type=Arrow] ID 2 {damage:3.5}') #Power 2 Enchantment
        response = rcon.send("execute @e[type=Arrow,score_ID_min=2,score_ID=2] ~ ~ ~ summon Creeper ~ ~ ~ {ignited:1,Fuse:1}")

        #Any arrows fired from the Teleport bow?
        rcon.send('scoreboard players set @e[type=Arrow] ID 3 {damage:4.0}') #Power 3 Enchantment
        response = rcon.send("testfor @e[type=Arrow,score_ID_min=3,score_ID=3]")
        if "Found Arrow" in response:
            orientation_y = mc.player.getRotation()
            orientation_x = mc.player.getPitch()
            if orientation_y < -180:
                orientation_y += 360
            if orientation_y > 180:
                orientation_y -= 360
            #effect <player> <effect> [seconds] [amplifier] [hideParticles]
            rcon.send("effect "+my_player_name+" minecraft:blindness 3 10 true")
            rcon.send("tp "+my_player_name+" @e[type=Arrow,score_ID_min=3,score_ID=3]")
            rcon.send("tp "+my_player_name+" ~ ~ ~ "+str(orientation_y)+" "+str(orientation_x))
            rcon.send("effect "+my_player_name+" clear")

        #Then remove the arrow.
        rcon.send("kill @e[type=Arrow,score_ID_min=1]")

    except:
        #if any errors occur from the server, ignore them
        pass



#CHALLENGE 1
# Modify the script above, and instead of summoning a snowman on the arrow, summon a lightning bolt.
# You'll need to look at the link below to see what the entity name is for snowman.
# http://technical-minecraft.wikia.com/wiki/Entity

#CHALLENGE 2
# Instead of summoning an entity, let's change the block.
# Here's an example of how it would look to summon water at the location of the arrow:
# response=rcon.send("execute @e[type=Arrow] ~ ~ ~ setblock ~ ~ ~ minecraft:flowing_water")
# Using this link: http://minecraft-ids.grahamedgecombe.com/
# Experiment with summoning various other blocks at the location, such as flowing lava.
# Note that in this case, instead of using the block ID as you have before, you need to use the
# more "human" name (e.g. minecraft:flowing_water)
