#!/usr/bin/env python


# mcpipy.com retrieved from URL below, written by SleepyOz
# http://www.raspberrypi.org/phpBB3/viewtopic.php?f=32&t=33427

import mcpi.block as block
import mcpi.minecraft as minecraft
import time
import server


"""
Dot matrix digits 5x8 matrix.
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

def output_digit(client, position, offset, dots):
    """
    Draw a digit in voxels.
    Client is the Minecraft connection.
    Position is the anchor point in Minecraft, a minecraft.Vec3.
    Offset is the number of the digit being drawn, starting at zero.
    Dots is an array of strings representing a digit.
    """
    x_offset = offset * 6 # Each digit is 5 voxels wide, plus 1 for a gap between digits.
    line_offset = 0 # Start at the top line.
    for line in dots: # For each line of each digit.
        dot_offset = 0 # Start at the left-most voxel.
        for dot in line: # For each voxel in the line.
            if dot == '0': # If voxel should be drawn.
                client.setBlock(position.x+dot_offset+x_offset, position.y-line_offset, position.z, block.ICE)
            else: # Voxel should be cleared.
                client.setBlock(position.x+dot_offset+x_offset, position.y-line_offset, position.z, block.AIR)
            dot_offset += 1 # Move over to the next voxel.

        # Each digit is 5 wide, but not all 5 voxels need to be supplied in the digit_dots, so blank out any that were not given.
        for blank in range(dot_offset, 5):
            client.setBlock(position.x+blank+x_offset, position.y-line_offset, position.z, block.AIR)
        line_offset += 1 # Next line.

client=minecraft.Minecraft.create(server.address) # Connect to Minecraft.
place=client.player.getPos() # Start near the player.
place.y += 9 # Above the player's ground level.

while True: # Repeat forever.
    timestr = time.strftime("%H:%M:%S") # Format time nicely.
    digit_offset = 0 # Start with the first digit.
    for letter in timestr: # For each symbol in the time.
        map = digit_dots[letter] # Get the dot map for the current digit.
        output_digit(client, place, digit_offset, map) # Draw the digit.
        digit_offset += 1 # Next digit.
    time.sleep(0.5) # Rest a while before drawing again.