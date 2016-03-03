spell_name = "Spell:Teleport"
spell_description = "Teleport to target location."
def execute_spell(mc, rcon, my_player_name):
    orientation_y = mc.player.getRotation()
    orientation_x = mc.player.getPitch()
    if orientation_y < -180:
        orientation_y += 360
    if orientation_y > 180:
        orientation_y -= 360
    #effect <player> <effect> [seconds] [amplifier] [hideParticles]
    rcon.send("effect "+my_player_name+" minecraft:blindness 3 10 true")
    rcon.send("tp "+my_player_name+" @e[type=Arrow]")
    rcon.send("tp "+my_player_name+" ~ ~ ~ "+str(orientation_y)+" "+str(orientation_x))
    rcon.send("effect "+my_player_name+" clear")


"""
y-rot (optional)
Specifies the horizontal rotation (-180.0 for due north, -90.0 for due east, 0.0 for due south, 90.0 for due west, to 179.9 for just west of due north, before wrapping back around to -180.0). Tilde notation can be used to specify a rotation relative to the target's previous rotation.
x-rot (optional)
Specifies the vertical rotation (-90.0 for straight up to 90.0 for straight down). Tilde notation can be used to specify a rotation relative to the target's previous rotation.
"""
