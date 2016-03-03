#!/usr/bin/env python

"""
Draw an analogue clock into Minecraft.
Use PIL to prepare the bitmaps, then update Minecraft.

SleepyOz: tfptfp(at)gmail.com
2013-02-13
"""

# mcpipy.com retrieved from URL below, written by SleepyOz
# http://www.raspberrypi.org/phpBB3/viewtopic.php?f=32&t=33427

import math
import mcpi.block as block
import mcpi.minecraft as minecraft
from PIL import Image # Remember to "sudo apt-get install python-imaging" to make PIL available.
from PIL import ImageDraw
import time
import server


# Not very good colour names, because they are inverting when displayed.
colour_black = 1
colour_dark = 32
colour_medium  = 64
colour_light = 128
colour_white = 192

def clockhand(angle, length):
    """
    Calculate the end point for the given vector.
    Angle 0 is 12 o'clock, 90 is 3 o'clock.
    Based around (32,32) as origin, (0,0) in top left.
    """
    radian_angle = math.pi * angle / 180.0
    x = 32 + length * math.cos(radian_angle)
    y = 32 + length * math.sin(radian_angle)
    return [(32,32),(x,y)]

def draw_clock():
    """
    Draw an analogue clock face.
    In an attempt to improve appearance, the clock is drawn at a higher
    resolution then scaled down with anti-aliasing.
    """
    now = time.localtime()

    bitmap = Image.new("L", (65,65), color=colour_black) # Work with oversized images, and reduce before displaying.
    draw = ImageDraw.Draw(bitmap) # An object to draw into.

    # Multiple outer rings so something survives the resolution reduction later.
    draw.ellipse((1,1,64,64), outline=colour_white) # Face.
    draw.ellipse((2,2,63,63), outline=colour_white) # Face.
    draw.ellipse((3,3,62,62), outline=colour_white) # Face.
    draw.ellipse((4,4,61,61), outline=colour_white) # Face.

    # TODO: We could draw numbers or chevrons on the clock face.

    # The hands are drawn by converting the time to degrees.
    # Note that all the hands move every second, althought the change might be too small to see.
    # The hour hand only moves every minute and even that is not visible.
    draw.line(clockhand(now.tm_hour * 30 + now.tm_min / 2, 20), fill=colour_white, width=4) # Hour hand.
    draw.line(clockhand(now.tm_min * 6 + now.tm_sec / 10, 22), fill=colour_white, width=3) # Minute hand.
    draw.line(clockhand(now.tm_sec * 6, 25), fill=colour_white, width=2) # Second hand.

    bitmap.thumbnail((32,32), Image.ANTIALIAS) # Reduce resolution to suit the view distance.
    return bitmap

class buffer:
    """
    Double-buffer a voxel block for Minecraft.
    To improve performance, only changes are actually sent to Minecraft.
    """
    anchor_position = minecraft.Vec3(0,0,0)
    offscreen = None
    onscreen = None

    def __init__(self, anchor_position):
        """
        Set everything up to render the voxels into the world
        at the given position.
        """
        self.anchor_position = anchor_position
        self.onscreen = Image.new("L", (32,32), color=0)

    def render(self):
        """
        Get a picture of the clock.
        """
        self.offscreen = draw_clock()

    def flip(self, client):
        """
        Put the off-screen buffer onto the screen.
        Only send the differences.
        Remember the new screen for use during the next flip.
        """
        if self.offscreen:
            width,height = self.offscreen.size
            draw = ImageDraw.Draw(self.onscreen) # So we can remember what we did for next time.
            for x in range(0, width - 1):
                for z in range(0, height - 1):
                    dot = self.offscreen.getpixel((x,z))
                    if self.onscreen.getpixel((x,z)) != dot:
                        # Change detected.
                        draw.point((x,z), fill=dot)

                        # Pick display items that suit the antialiasing.
                        display = block.SNOW_BLOCK # Very white.
                        if (dot >= colour_dark+16) and (dot < colour_medium + 16):
                            display = block.WOOL # Light grey.
                        elif (dot >= colour_medium + 16) and (dot < colour_light + 16):
                            display = block.STONE # Medium grey.
                        elif (dot >= colour_light + 16):
                            display = block.OBSIDIAN # Blackish.

                        client.setBlock(self.anchor_position.x + x, self.anchor_position.y, self.anchor_position.z + z, display)

client=minecraft.Minecraft.create(server.address) # Connect to Minecraft.
place=client.player.getPos() # Start near the player.
place.y += 0 # At the level of the player's feet.
bitmapper = buffer(place)

while True:
    bitmapper.render()
    bitmapper.flip(client)
    time.sleep(.1) # Rest a while before drawing again.