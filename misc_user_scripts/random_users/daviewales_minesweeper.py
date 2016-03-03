#!/usr/bin/env python

# mcpipy.com retrieved from URL below, written by Davie Wales
# https://bitbucket.org/dwales/minesweeper-for-minecraft-pi-edition/src


import sys
import random
import threading
import mcpi.minecraft as minecraft
import server


defaultDifficulty = 0.1
setDifficulty = defaultDifficulty

class board:
    """ The cartesian grid can be done as follows:
    board = [["?", "*", "?", "?", "*", "?", "?", "?", "?", "*",], 
            ["?", "?", "*", "?", "?", "?", "?", "?", "?", "?",], 
            ["?", "*", "*", "?", "*", "?", "?", "*", "*", "?",], 
            ["?", "?", "?", "?", "?", "?", "*", "?", "*", "?",],
            ["*", "?", "?", "?", "?", "*", "?", "?", "?", "?",], 
            ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?",], 
            ["?", "*", "?", "*", "?", "?", "?", "*", "?", "*",], 
            ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?",],
            ["?", "*", "?", "?", "*", "*", "?", "?", "*", "?",], 
            ["?", "?", "*", "?", "?", "?", "?", "*", "?", "?",]]

     Obviously the grid will be randomly generated on run to fit 
     within the bounds of the terminal window.
     Notice that you can access the state of any tile on the grid with
     the simple command "board[x][y]"
     i.e. a = board[0][0] makes a == "?", a = board[0][9] makes a == "*"
     NOTE: I subsequently changed the code to use nested dictionaries,
     rather than lists to represent the board. The general idea is
     still the same...
     If we use a dictionary rather than a list in the following
     function, we will get a KeyError if we try to access a 
     negative index, assuming we construct the dictionary such
     that it has identical indexes to the list equivalent.
     i.e. dictionary = {0:{0:" ", 1:" ", 2"*"}, 1:{0:"*", 1:" ", 2:" "}}
     This will be helpful, as it will negate the need to explicitly
     check whether a particular coordinate is legitimate. i.e. a 
     dictionary won't match negative values for x, y, but a list will..."""

    """ At the moment we are getting the window size before curses is
     initialised, which means that we have to use "stty size". If 
     we can move this code into the curses section, we can use the
     built in window.getmaxyx(). This will make it easier to use
     windows smaller than the size of the terminal for the game, 
     which will in turn allow us to add timers and minecounts."""

    def __init__(self):
        global width, height
        width = 10
        height = 10

    def options(self):
        totalTiles = width * height

        #possible choices of tile: either "*" or " "
        self.mineNumber = int(setDifficulty * totalTiles)
        choices = list(self.mineNumber * "*")
        choices.extend(list((totalTiles-len(choices))*" "))
        return choices

    # For every x and y, check all the squares around to see if there is a mine,
    # add together the number of mines touching the original square and replace
    # the original square with the final count.
    def numberise(self, board):
        for x in xrange(width):
            for y in xrange(height):
                count = 0
                if board[x][y] != "*":
                        for i in xrange(-1, 2):
                            for n in xrange(-1, 2):
                                try:
                                    if board[x+i][y+n] == "*":
                                        count += 1
                                except KeyError:
                                    pass
                        if count != 0:
                            board[x][y] = str(count)

    def create(self):
        self.mineCoords = []
        choices = self.options()
        board = {}
        for i in xrange(0, width):
            board[i] = {}
            for n in xrange(0, height):
                board[i][n] = choices.pop(choices.index(random.choice(choices)))
                if board[i][n] == "*":
                    self.mineCoords.append([i,n])

        self.numberise(board)
        for i in xrange(width):
            for n in xrange(height):
                minecraftAddBlock(i, n, 1, board[i][n])

        return board

    def visibleScreen(self):
        board = {}
        for i in xrange(0, width):
            board[i] = {}
            for n in xrange(0, height):
                board[i][n] = " "
        return board

def minecraftAddBlock(X, Y, Z, mineAttribute):
    # This equates values passed through mineAttribute with the actual
    # block IDs from Minecraft.
    # 0 is Air, 5 is Wood Planks, 4 is cobblestone, coal is 16
    # Iron is 15, Gold is 14, Diamond is 56, Gold Block is 41, 
    # Diamond Block is 57
    mineDict = {"dirt":3, "*":46, " ":20, 0:0, "1":5, "2":4, "3":16, "4":15, "5":14, "6":56, "7":41, "8":57}
    mc.setBlock(X, Y, Z, mineDict[mineAttribute])

def explore(x, y, Z): # Z is capitalised because it doesn't
                              # need to be changed by the function.
    """ This is the bit that happens when you click on a blank square
     First it checks the squares directly around the clicked square
     If the square it checks is a number, it will display it, and
     if the square it checks is blank, it will add the blank square's
     coordinates to a list or dictionary, then it will keep doing the
     same process to all the coordinates in the list, deleting squares
     that have been checked, and adding new squares, until the list is
     empty. At that point, the area around the original square will be
     revealed, as you would expect to happen in minesweeper."""

    checked = [[x,y]]       # Has been checked and contains either a number or ' '
    toBeCentre = [[x, y]]   # Each point in this list will be checked on all sides for the above conditions
    centred = []            # These points have already been checked on all sides
    global cleared
    cleared = []

    while len(toBeCentre) > 0:
        X, Y = toBeCentre.pop(0)
        centred.append([X,Y])
        minecraftAddBlock(X, Y, Z, 0)
        if [X,Y] not in cleared:
            cleared.append([X,Y])
        for i in xrange(-1, 2):
            for n in xrange(-1, 2):

        # When I was writing this section, it wouldn't work, and wouldn't work
        # and then after changing it around a million times, suddenly it started working...
        # The only problem is that I don't actually know what I did to make it work... =P
                try:
                    if ((newBoard[X+i][Y+n] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])and ([X+i, Y+n] not in checked)):
                        minecraftAddBlock(X+i, Y+n, Z, 0) #newBoard[X+i][Y+n])
                        checked.append([X+i, Y+n])
                        if [X+i,Y+n] not in cleared:
                            cleared.append([X+i,Y+n])

                    elif newBoard[X+i][Y+n] == " ":
                        if (([X+i, Y+n] not in checked) and ([X+i, Y+n] not in toBeCentre)):
                            toBeCentre.append([X+i, Y+n])
                            checked.append([X+i, Y+n])
                except KeyError:
                    pass

class WinningCheckThread (threading.Thread):

    def __init__(self,  mineCoords, mineNumber, z):
        self.mineCoords = mineCoords
        self.mineNumber = mineNumber
        self.z = z
        threading.Thread.__init__(self)

    def run(self):
        global running
        running = True
        mc = minecraft.Minecraft.create()
        while running:
            ### This is the winning condition... ###
            flagCount = 0
            correctFlagCount = 0

            for x in xrange(width):
                for y in xrange(height):
                    if mc.getBlock(x, y, 0-1) == 50:
                        flagCount += 1
                        if [x,y] in self.mineCoords:
                            correctFlagCount += 1

            if  (self.mineNumber == correctFlagCount) and (self.mineNumber == flagCount):
                for x in xrange(width):
                     for y in xrange(height):
                         mc.setBlock(x, y, self.z, 20)

                mc.postToChat("You Win!!!")
                running = False
                sys.exit()

class BlockCheckThread(threading.Thread):

    def __init__(self):

        threading.Thread.__init__(self)
    def run(self):
        global running
        running = True
        mc = minecraft.Minecraft.create()
        while running:

            event = mc.events.pollBlockHits()

            if event:
#                mc.postToChat("Hit detected")
                eventSplit = str(event[0]).split()
                eventSplit = [eventSplit[1][0], eventSplit[2][0], eventSplit[3][0]]
                cursorX, cursorY, cursorZ = eventSplit
                cursorX = int(cursorX)
                cursorY = int(cursorY)
                cursorZ = int(cursorZ)
                if newBoard[cursorX][cursorY] == "*":
                    for y in xrange(height):
                        for x in xrange(width):
                            # This bit of code's dodgy, because it relies on the 
                            # creation of "newBoard" external to the function...
                            mc.setBlock(x, y, z, 0) # (If you hit a mine it clears the board.)
                    mc.postToChat("You Lose!")
                    running = False
                    sys.exit()

                if newBoard[cursorX][cursorY] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    #visibleScreen[x][y] = newBoard[x][y]
                    mc.setBlock(cursorX, cursorY, cursorZ, 0) # We just remove the top layer.

                if newBoard[cursorX][cursorY] == " ":
                    explore(cursorX, cursorY, cursorZ)

#def main():
global running
running = True
mc = minecraft.Minecraft.create(server.address)
board = board()
newBoard = board.create()
visibleScreen = board.visibleScreen()

for x in xrange(width):
    for y in xrange(height):
        mc.setBlock(x,y,-1,0)

z = 0 # For now... We can make this dynamic later.
for y in xrange(height):
   for x in xrange(width):
       # This bit of code's dodgy, because it relies on the 
       # creation of "visibleScreen" external to the function...
       minecraftAddBlock(x, y, z, "dirt")

WinningCheck = WinningCheckThread(board.mineCoords, board.mineNumber, z)
BlockCheck = BlockCheckThread()
BlockCheck.daemon
WinningCheck.start()
BlockCheck.start()

#main()