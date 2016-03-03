spell_name = "Spell:Lava"
spell_description = "Create a volcanic eruption."
def execute_spell(mc, rcon, my_player_name):
    response = rcon.send("execute @e[type=Arrow] ~ ~ ~ setblock ~ ~ ~ minecraft:flowing_lava")
