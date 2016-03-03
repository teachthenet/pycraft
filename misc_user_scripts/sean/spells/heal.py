spell_name = "Spell:Heal"
spell_description = "Heal all allied targets over 5 seconds."
def execute_spell(mc, rcon, my_player_name):
    #effect <player> <effect> [seconds] [amplifier] [hideParticles]
    rcon.send("effect @e[type=Player] minecraft:regeneration 5 2 true")