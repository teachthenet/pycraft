from mcpi import minecraft
import rcon_mc.rcon
import rcon_mc.lib.msocket

server_address = "162.244.165.151"
rcon_port = 25575
rcon_password = "pycraft"
raspberry_juice_port = 4711
my_player_name = "seanybob"

mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)
rcon = rcon_mc.rcon.client(server_address, rcon_port, rcon_password)

spell_name = "Spell:Lightning"
spell_description = "Create a bolt of lightning."

#Grant player bows to trigger spells
rcon.send('give '+my_player_name+' minecraft:bow 1 0 {display:{Name:"'+spell_name+'",Lore:["'+spell_description+'"]},ench:[{id:51,lvl:1},{id:34,lvl:100}]}')

#Give player arrows to use with the bow
rcon.send('give '+my_player_name+' minecraft:arrow 1 0')

#Watch for spellcasts
while True:

    try:

        #If we see an arrow...
        response=rcon.send("testfor @e[type=Arrow]")

        """
        #improvements
        /give @p minecraft:tipped_arrow 1 0 {Potion:"minecraft:invisibility"}
        /testfor @e[type=Arrow] {Potion:"minecraft:harming"}
        /testfor @e[type=Arrow] {CustomName:"Ice Arrow"} #You should also know that an arrow doesn't keep its item name after being fired. It'll only work if the arrow was summoned with the name.
        http://www.minecraftforum.net/forums/minecraft-discussion/redstone-discussion-and/2085300-how-to-test-if-an-arrow-has-been-shot-by-a
        http://www.minecraftforum.net/forums/minecraft-discussion/redstone-discussion-and/2085233-help-me-with-a-redstone-problem#entry31586426



        scoreboard objectives add ID dummy
        scoreboard players set @e[type=Arrow] ID 1 {damage:3.0}
        execute @e[type=Arrow,score_ID_min=1,score_ID=1] ~ ~ ~ summon Fireball ~ ~ ~ {ExplosionPower:3,direction:[]}



        """
        #Improvements: http://www.minecraftforum.net/forums/minecraft-discussion/redstone-discussion-and/2556776-test-for-named-or-tipped-arrows
        
        if "Found Arrow" in response:

            #Summon a lightning bolt on the arrow!
            response = rcon.send("execute @e[type=Arrow] ~ ~ ~ summon LightningBolt")

            #Then remove the arrow.
            rcon.send("kill @e[type=Arrow]")

    except rcon_mc.rcon.RconException:
        #if any errors occur from the server, ignore them
        pass


#CHALLENGE 1
# Modify the script above, and instead of summoning a lightning bolt on the arrow, summon a snowman.
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
