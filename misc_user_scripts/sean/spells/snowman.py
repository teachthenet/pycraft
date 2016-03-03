spell_name = "Spell:Snowman"
spell_description = "Frosty the Snowman, was alive as he could be..."
def execute_spell(mc, rcon, my_player_name):
    response = rcon.send("execute @e[type=Arrow] ~ ~ ~ summon SnowMan")
