"""
This script does the following:
- Take an image as input, and read it pixel by pixel.
- For each pixel in the image, set a block in the minecraft world closest to the color of that pixel.
- End result should be pixel art in minecraft world.
- Use mario.gif in this directory to start with.

Try to understand how this script works - it uses various data structures and functions.

Try to figure out how it takes an image as input, and change the image to something else you'd like to insert into the minecraft world.

NOTE! This script requires installing the Python library 'pillow' - instructions located here:
https://pillow.readthedocs.org/en/latest/installation.html
"""

import sys
sys.path.append("../")

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="seanybob") #NOTE - replace "seanybob" with your name

from math import sqrt

from PIL import Image

# Possible blocks  in (Name, ID, (RGB1,RGB2,..),Data)
	#RGBs are used to color match. 
possibleBlocks = (
    ("Air", 0, ( (0, 136, 255) ,),0),
    ("Smooth Stone", 1, ( (125,125, 125) ,),0),
    ("Dirt", 3, ( (133,96,66),),0), 
    ("Cobblestone", 4, ( (117,117,117),),0), 
    ("Wooden Plank", 5, ( (156,127,78),),0), 
    ("Bedrock", 7, ( (83,83,83),),0), 
    ("Sand", 12, ( (217,210,158),),0), 
    ("Gravel", 13, ( (136, 126, 125),),0), 
    ("Gold Ore", 14, ( (143,139,124),),0), 
    ("Iron Ore", 15, ( (135,130,126),),0), 
    ("Coal Ore", 16, ( (115,115,115),),0), 
    ("Wood", 17, ( (154,125,77),),0), 
    ("Sponge", 19, ( (182,182,57),),0), 
    ("White Wool", 35, ( (221,221,221),),0), 
    ("Orange Wool", 35, ( (233,126,55),),1), 
    ("Magenta Wool", 35, ( (179,75,200),),2), 
    ("Light Blue Wool", 35, ( (103,137,211),),3), 
    ("Yellow Wool", 35, ( (192,179,28),),4), 
    ("Light Green Wool", 35, ( (59,187,47),),5), 
    ("Pink Wool", 35, ( (217,132,153),),6), 
    ("Dark Gray Wool", 35, ( (66,67,67),),7), 
    ("Gray Wool", 35, ( (157,164,165),),8), 
    ("Cyan Wool", 35, ( (39,116,148),),9), 
    ("Purple Wool", 35, ( (128,53,195),),10), 
    ("Blue Wool", 35, ( (39,51,153),),11), 
    ("Brown Wool", 35, ( (85,51,27),),12), 
    ("Dark Green Wool", 35, ( (55,76,24),),13), 
    ("Red Wool", 35, ( (162,44,42),),14), 
    ("Black Wool", 35, ( (26,23,23),),15), 
    ("Gold", 41, ( (249,236,77),),0), 
    ("Iron", 42, ( (230,230,230),),0), 
    ("TwoHalves", 43, ( (159,159,159),),0),
    ("Brick", 45, ( (155,110,97),),0), 
    ("Mossy Cobblestone", 48, ( (90,108,90),),0), 
    ("Obsidian", 49, ( (20,18,29),),0), 
    ("Diamond Ore", 56, ( (129,140,143),),0), 
    ("Diamond Block", 57, ( (99,219,213),),0), 
    ("Workbench", 58, ( (107,71,42),),0), 
    ("Redstone Ore", 73, ( (132,107,107),),0), 
    ("Snow Block", 80, ( (239,251,251),),0), 
    ("Clay", 82, ( (158,164,176),),0), 
    ("Jukebox", 84, ( (107,73,55),),0), 
    ("Pumpkin", 86, ( (192,118,21),),0), 
    ("Netherrack", 87, ( (110,53,51),),0), 
    ("Soul Sand", 88, ( (84,64,51),),0), 
    ("Glowstone", 89, ( (137,112,64),),0) 
)

def getBlockFromColor(RGB):
	smallestDistIndex = -1
	smallestDist = 300000
	curIndex = 0
	for block in possibleBlocks:
		for blockRGB in block[2]:
			curDist = getColorDist(RGB, blockRGB)
		
			if (curDist < smallestDist):
				smallestDist = curDist
				smallestDistIndex = curIndex

		curIndex = curIndex + 1
	
	if (smallestDistIndex == -1):
		return -1
		
	return possibleBlocks[smallestDistIndex]
	
def getColorDist(colorRGB, blockRGB):
	return sqrt( pow(colorRGB[0]-blockRGB[0],2) + pow(colorRGB[1]-blockRGB[1],2) + pow(colorRGB[2]-blockRGB[2],2))
	
pos = mc.player.getPos()

maxsize = (100, 100)

im = Image.open('mario.gif')
im.thumbnail(maxsize, Image.ANTIALIAS)
rgb_im = im.convert('RGB')
rows, columns = rgb_im.size
print rows, columns
for r in range(rows):
    for c in range(columns):
        rgb = rgb_im.getpixel((r, c))
        mc_block = getBlockFromColor(rgb)
        mc.setBlock(pos.x+r, pos.y, pos.z+c, mc_block[1])
