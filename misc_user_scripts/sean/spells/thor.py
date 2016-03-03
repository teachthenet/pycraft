spell_name = "Spell:Thor"
spell_description = "Wield the power of the thunder god."
def execute_spell(mc, rcon, my_player_name):
    response = rcon.send("execute @e[type=Arrow] ~ ~ ~ execute @e[r=50] ~ ~ ~ summon LightningBolt")