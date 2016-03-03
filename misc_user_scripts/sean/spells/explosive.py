spell_name = "Spell:Explosive"
spell_description = "Create an explosion."
def execute_spell(mc, rcon, my_player_name):
    response = rcon.send("execute @e[type=Arrow] ~ ~ ~ summon Creeper ~ ~ ~ {ignited:1,Fuse:1}")
