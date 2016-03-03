# Don't execute this directory -- this is a support script for danielbates_setblockdemo.py

import sys

# Add some common locations where the main API might be. Feel free to add/change
# these to suit you.
sys.path.append("mcpi")
sys.path.append("api/python/mcpi")
sys.path.append("mcpi/api/python/mcpi")

# Attempt to import Mojang's API.
try:
	import connection
	import minecraft
except ImportError:
	print "Unable to find Minecraft API. Please place minecraft_basic.py in the mcpi directory."
	exit()

_server = None
_blockedit = None
_playeredit = None

def connect(ip="127.0.0.1", port=4711):
	global _server, _blockedit, _playeredit
	
	try:
		_server = connection.Connection(ip, port)
		_blockedit = minecraft.Minecraft(_server)
		_playeredit = _blockedit.player
	except Exception:
		print "Unable to connect to Minecraft server at {0}:{1}".format(ip,port)
		return

	print "Connected to Minecraft server at {0}:{1}".format(ip,port)

def setblock(x,y,z,*typedata):
	_blockedit.setBlock(x,y,z,typedata)

def getblock(x,y,z):
	return _blockedit.getBlock(x,y,z)

def moveplayer(x,y,z):
	_playeredit.setPos(x,y,z)

AIR = 0
STONE = 1
GRASS = 2
DIRT = 3
COBBLESTONE = 4
WOOD_PLANK = 5
SAPLING = 6
BEDROCK = 7
WATER_FLOWING = 8
WATER = 9
LAVA_FLOWING = 10
LAVA = 11
SAND = 12
GRAVEL = 13
GOLD_ORE = 14
IRON_ORE = 15
COAL_ORE = 16
WOOD = 17
LEAVES = 18
GLASS = 20
LAPIS_ORE = 21
LAPIS = 22
SANDSTONE = 24
BED = 26
COBWEB = 30
TALL_GRASS = 31
WOOL = 35
FLOWER_YELLOW = 37
FLOWER_RED = 38
MUSHROOM_BROWN = 39
MUSHROOM_RED = 40
GOLD = 41
IRON = 42
STONE_SLAB_DOUBLE = 43
STONE_SLAB = 44
BRICK = 45
TNT = 46
BOOKSHELF = 47
MOSSY_STONE = 48
TORCH = 50
FIRE = 51
WOOD_STAIRS = 53
CHEST = 54
DIAMOND_ORE = 56
DIAMOND = 57
CRAFTING_TABLE = 58
FARMLAND = 60
FURNACE = 61
FURNACE_ACTIVE = 62
WOOD_DOOR = 64
LADDER = 65
COBBLESTONE_STAIRS = 67
IRON_DOOR = 71
REDSTONE_ORE = 73
SNOW_COVER = 78
ICE = 79
SNOW = 80
CACTUS = 81
CLAY = 82
SUGAR_CANE = 83
FENCE = 85
GLOWSTONE = 89
INVISIBLE_BEDROCK = 95
STONE_BRICK = 98
GLASS_PANE = 102
MELON = 103
FENCE_GATE = 107
GLOWING_OBSIDIAN = 246
NETHER_REACTOR_CORE = 247
UPDATE_GAME_BLOCK = 249