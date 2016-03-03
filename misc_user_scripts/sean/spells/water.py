spell_name = "Spell:Water"
spell_description = "Create a spring of water."
def execute_spell(mc, rcon, my_player_name):
    response=rcon.send("execute @e[type=Arrow] ~ ~ ~ setblock ~ ~ ~ minecraft:flowing_water")
