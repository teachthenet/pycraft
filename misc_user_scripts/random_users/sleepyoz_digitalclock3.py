#!/usr/bin/env python


# mcpipy.com retrieved from URL below, written by SleepyOz
# http://www.raspberrypi.org/phpBB3/viewtopic.php?f=32&t=33427

import mcpi.block as block
import mcpi.minecraft as minecraft
import time
import server


"""
Dot matrix digits 5 wide by 8 high.
0 - voxel should be drawn
Anything else - voxel should be cleared
"""
digit_dots = {
    '0':[
        ' 000',
        '0   0',
        '0   0',
        '0   0',
        '0   0',
        '0   0',
        '0   0',
        ' 000',
        ],
    '1':[
        '  0',
        ' 00',
        '  0',
        '  0',
        '  0',
        '  0',
        '  0',
        ' 000',
        ],
    '2':[
        ' 000',
        '0   0',
        '   0',
        '  0',
        ' 0',
        '0',
        '0',
        '00000',
        ],
    '3':[
        ' 000',
        '0   0',
        '    0',
        '  00',
        '    0',
        '    0',
        '0   0',
        ' 000',
        ],
    '4':[
        '   0',
        '  00',
        ' 0 0',
        '0  0',
        '00000',
        '   0',
        '   0',
        '   0',
        ],
    '5':[
        '00000',
        '0',
        '0',
        '0000',
        '    0',
        '    0',
        '0   0',
        ' 000',
        ],
    '6':[
        ' 000',
        '0   0',
        '0',
        '0000',
        '0   0',
        '0   0',
        '0   0',
        ' 000',
        ],
    '7':[
        '00000',
        '    0',
        '   0',
        '  0',
        ' 0',
        '0',
        '0',
        '0',
        ],
    '8':[
        ' 000',
        '0   0',
        '0   0',
        ' 000',
        '0   0',
        '0   0',
        '0   0',
        ' 000',
        ],
    '9':[
        ' 000',
        '0   0',
        '0   0',
        ' 0000',
        '    0',
        '    0',
        '0   0',
        ' 000',
        ],
    ':':[
        '',
        '',
        '  00',
        '  00',
        '',
        '  00',
        '  00',
        '',
        ],
    }

class buffer:
    """
    Double-buffer a voxel message for Minecraft.
    To improve performance, only changes are rendered.
    """
    anchor_position = minecraft.Vec3(0,0,0)
    last_message = ''
    offscreen = []
    onscreen = []
    unset = block.OBSIDIAN
    set = block.SNOW_BLOCK

    def __init__(self, anchor_position):
        """
        Set everything up to render messages into the world
        at the given position.
        """
        self.anchor_position = anchor_position

    def draw_base(self, client):
        """
        Build some foundations for the clock.
        """
        # Foundations of stone.
        for y in range(-5, -1): # Nice thick base.
            for x in range(-1, 8*6): # 8 digits each 6 wide, plus a border, minus one to cut out the space beside the last digit.
                for z in range(-1, 8+1): # Each digit is 8 high, plus a border.
                    client.setBlock(self.anchor_position.x+x, self.anchor_position.y+y, self.anchor_position.z+z, block.STONE)
            # Shallow pool at the top.
        for x in range(0, 8*6-1):
            for z in range(0, 8):
                client.setBlock(self.anchor_position.x+x, self.anchor_position.y-2, self.anchor_position.z+z, block.WATER_STATIONARY)

    def render(self, message):
        """
        Put message into the off-screen buffer.
        """
        if message != self.last_message: # Do nothing if the message has not changed.
            self.last_message =  message # For next time.

            self.offscreen = [] # Clear any previous use of the buffer.
            letter_offset = 0
            for letter in message:
                rendition = digit_dots[letter]
                line_offset = 0
                for line in rendition:
                    if len(self.offscreen) <= line_offset:
                        # Make space to store the drawing.
                        self.offscreen.append([])
                    dot_offset = 0
                    for dot in line:
                        if dot == '0':
                            self.offscreen[line_offset].append(self.set)
                        else:
                            self.offscreen[line_offset].append(self.unset)
                        dot_offset += 1
                    for blank in range(dot_offset, 6):
                        # Expand short lines to the full width of 6 voxels.
                        self.offscreen[line_offset].append(self.unset)
                    line_offset += 1
                letter_offset += 1

            # Clear the onscreen buffer.
            # Should only happen on the first call.
            # Assumption: message will always be the same size.
            # Assumption: render() is called before flip().
            if self.onscreen == []:
                # No onscreen copy yet - so make it the same size as the offscreen image. Fill with suitable voxels.
                line_offset = 0
                for line in self.offscreen:
                    self.onscreen.append([])
                    for dot in line:
                        self.onscreen[line_offset].append(block.DIRT)
                    line_offset += 1

    def flip(self, client):
        """
        Put the off-screen buffer onto the screen.
        Only send the differences.
        Remember the new screen for next flip.
        Draw the clock inverted so it read properly from above.
        """
        line_offset = 0
        height = len(self.offscreen) - 1
        for line in self.offscreen:
            dot_offset = 0
            length = len(line) - 2 # Fit into the border better.
            for dot in line:
                if self.onscreen[line_offset][dot_offset] != dot:
                    self.onscreen[line_offset][dot_offset] = dot
                    client.setBlock(self.anchor_position.x+length-dot_offset, self.anchor_position.y-3, self.anchor_position.z+height-line_offset, dot)
                dot_offset += 1
            line_offset += 1

client=minecraft.Minecraft.create(server.address) # Connect to Minecraft.
place=client.player.getPos() # Start near the player.
# place.y is just below the player, and we don't need to change it.
bitmapper = buffer(place)

bitmapper.draw_base(client)
while True:
    timestr = time.strftime("%H:%M:%S") # Format time nicely.
    bitmapper.render(timestr)
    bitmapper.flip(client)
    time.sleep(.1) # Rest a while before drawing again.