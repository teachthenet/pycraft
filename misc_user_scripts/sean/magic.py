import sys
sys.path.append("../../")
from mcpi import minecraft
import random
import time
import os

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


#Import spells
spells = []
for filename in os.listdir("./spells/"):
    if os.path.isfile("./spells/"+filename) and filename not in ["__init__.py"] and filename[-2:] == "py":
        module_name = filename.replace(".py", "")
        exec "from spells import "+module_name.replace(".py", "")
        spells.append({
            "spell_name": eval(module_name+".spell_name"),
            "spell_description": eval(module_name+".spell_description"),
            "execute_spell": eval(module_name+".execute_spell")
        })

#Grant player bows to trigger spells
rcon.send('clear '+my_player_name)
for spell in spells:
    rcon.send('give '+my_player_name+' minecraft:bow 1 0 {display:{Name:"'+spell['spell_name']+'",Lore:["'+spell['spell_description']+'"]},ench:[{id:51,lvl:1},{id:34,lvl:100}]}')

rcon.send('give '+my_player_name+' minecraft:arrow 1 0')

rcon.send("gamemode 0 "+my_player_name)
gamemode = 0

#Watch for spellcasts
while True:
    try:
        response=rcon.send("testfor @e[type=Arrow]")
        if "Found Arrow" in response:

            for spell in spells:
                response=rcon.send('testfor @p {SelectedItem:{id:minecraft:bow,tag:{display:{Name:"'+spell['spell_name']+'"}}}}')
                if "Found" in response:
                    spell['execute_spell'](mc, rcon, my_player_name)
                    rcon.send("kill @e[type=Arrow]")
    except:
        pass

    try:
        #Special test for "god" mode.
        response=rcon.send('testfor @p {SelectedItem:{id:minecraft:bow,tag:{display:{Name:"Spell:Thor"}}}}')
        if gamemode == 0 and "Found" in response:
            rcon.send("gamemode 1 "+my_player_name)
            gamemode = 1
            rcon.send("effect "+my_player_name+" minecraft:night_vision 9999 10 true")
        elif gamemode == 1 and "Found" not in response:
            rcon.send("gamemode 0 "+my_player_name)
            gamemode = 0
            rcon.send("effect "+my_player_name+" clear")
    except:
        pass

    