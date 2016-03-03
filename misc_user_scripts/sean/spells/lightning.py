spell_name = "Spell:Lightning"
spell_description = "Create a bolt of lightning."
def execute_spell(mc, rcon, my_player_name):
    response = rcon.send("execute @e[type=Arrow] ~ ~ ~ summon LightningBolt")
