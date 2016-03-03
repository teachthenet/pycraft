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

    def __init__(self, anchor_position):
        """
        Set everything up to render messages into the world
        at the given position.
        """
        self.anchor_position = anchor_position

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
                            self.offscreen[line_offset].append(block.ICE)
                        else:
                            self.offscreen[line_offset].append(block.AIR)
                        dot_offset += 1
                    for blank in range(dot_offset, 6):
                        # Expand short lines to the full width of 6 voxels.
                        self.offscreen[line_offset].append(block.AIR)
                    line_offset += 1
                letter_offset += 1

            # Clear the onscreen buffer.
            # Should only happen on the first call.
            # Assumption: message will always be the same size.
            # Assumption: render() is called before flip().
            if self.onscreen == []:
                # No onscreen copy - so make it the same size as the offscreen image. Fill with AIR voxels.
                line_offset = 0
                for line in self.offscreen:
                    self.onscreen.append([])
                    for dot in line:
                        self.onscreen[line_offset].append(block.AIR)
                    line_offset += 1

    def flip(self, client):
        """
        Put the off-screen buffer onto the screen.
        Only send the differences.
        Remember the new screen for next flip.
        """
        line_offset = 0
        for line in self.offscreen:
            dot_offset = 0
            for dot in line:
                if self.onscreen[line_offset][dot_offset] != dot:
                    self.onscreen[line_offset][dot_offset] = dot
                    client.setBlock(self.anchor_position.x+dot_offset,self.anchor_position.y-line_offset,self.anchor_position.z, dot)
                dot_offset += 1
            line_offset += 1

client=minecraft.Minecraft.create(server.address) # Connect to Minecraft.
place=client.player.getPos() # Start near the player.
place.y += 9 # Above the player's ground level.
bitmapper = buffer(place)

while True:
    timestr = time.strftime("%H:%M:%S") # Format time nicely.
    bitmapper.render(timestr)
    bitmapper.flip(client)
    time.sleep(.1) # Rest a while before drawing again.