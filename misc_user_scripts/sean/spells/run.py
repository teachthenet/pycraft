spell_name = "Spell:Run"
spell_description = "Give all players a speed boost for 5 seconds."
def execute_spell(mc, rcon, my_player_name):
    #effect <player> <effect> [seconds] [amplifier] [hideParticles]
    rcon.send("effect @e[type=Player] minecraft:speed 5 3 true")