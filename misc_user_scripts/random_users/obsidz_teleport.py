#!/usr/bin/env python

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import server


#Author:		Obsidz
#
#Description:   This is a teleport pad script.
#			   To create a pad, place a nether reactor core onto a location and ring with cobbledtone blocks
#			   To add to locations list walk over it
#
#Notes:		 Pads added to list by walking over them
#			   Pads not removed if destroyed but can be teleported to but not from
#			   You cannot teleport to the same pad without modifying script
#			   Pads need to be added each time the script is run

# modified version - as shared on mcpipy.com
# original post @ http://www.minecraftforum.net/topic/1691618-teleportation-python-script/

LPLoc = list()
 
Pads = 0
Cpad = 0

# If you are running this script with the bukkit mod, then use a diamond block as the magic center block for teleporting
# comment/uncomment below as appropriate
magic_block = block.DIAMOND_BLOCK.id # for bukkit server
#magic_block = block.NETHER_REACTOR_CORE.id # for raspberry pi

def isLaunchPad(): #checks if the the location below the player is a teleporting pad
		loc = mc.player.getPos()
		if ((mc.getBlock(loc.x,loc.y-1,loc.z) == magic_block) and
			(mc.getBlock(loc.x-1,loc.y-1,loc.z-1) == block.COBBLESTONE.id) and
			(mc.getBlock(loc.x-1,loc.y-1,loc.z) == block.COBBLESTONE.id) and
			(mc.getBlock(loc.x-1,loc.y-1,loc.z+1) == block.COBBLESTONE.id) and
			(mc.getBlock(loc.x,loc.y-1,loc.z+1) == block.COBBLESTONE.id) and
			(mc.getBlock(loc.x,loc.y-1,loc.z-1) == block.COBBLESTONE.id) and
			(mc.getBlock(loc.x+1,loc.y-1,loc.z-1) == block.COBBLESTONE.id) and
			(mc.getBlock(loc.x+1,loc.y-1,loc.z) == block.COBBLESTONE.id) and
			(mc.getBlock(loc.x+1,loc.y-1,loc.z+1) == block.COBBLESTONE.id)):
			addLPLoc(loc)
			return True
		else:
			return False
def addLPLoc(Vec3): #Loggs the location of the pad for future use
	global Pads
	global LPLoc
   
	inList = False
	if Pads > 0:
		for loc in LPLoc:
			if (loc.x == Vec3.x and loc.y == Vec3.y and loc.z == Vec3.z):
				inList = True
			   
	if not inList:
		LPLoc.append(Vec3)
		mc.postToChat("I'll remember this pad location!")
		Pads =  len(LPLoc)
def locCheck(): #Checks that you are not teleporting to the same pad
   
	global Cpad
	global LPLoc
	loc = mc.player.getPos()
	if (loc.x == LPLoc[Cpad].x and loc.y == LPLoc[Cpad].y and loc.z == LPLoc[Cpad].z):
		Cpad = Cpad + 1
def TPChar(): #sends the character to the next pad
	global Pads
	global Cpad
	global LPLoc
   
	if Pads > 1:
		mc.player.setPos(LPLoc[Cpad].x,LPLoc[Cpad].y + 1,LPLoc[Cpad].z)
		Cpad = ( Cpad + 1) %  Pads
		time.sleep(3.0)
   
if __name__ == "__main__": # The script
   
	mc = minecraft.Minecraft.create(server.address)
	while True:
		if isLaunchPad():
			TPChar()
   
		time.sleep(0.1)