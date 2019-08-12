import numpy as np
import copy

#https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

class Game:
    def __init__(self, width=6, height=6, beacon=None):
        self.board_size = (width, height)
        if beacon is None:
            self.beacon = np.zeros(self.board_size)
        else:
            self.beacon = beacon
        self.state = self.beacon


    def _numNeighbors(self, x, y, debugMode=0):
        if debugMode == 1:
            print '---Game.py _numNeighbours ---'
            print 'Debug Mode: ON'
            print ' x=' + str(x) + ' y=' + str(y)
            print self.state
        startX = 0
        startY = 0
        endX = 0
        endY = 0
        neighbors = 0
        boardWidth = self.board_size[0]
        boardHeight = self.board_size[1]
        if debugMode ==1:
            print 'Board width = ' + str(boardWidth) + ' height = ' + str(boardHeight)

        if (x > 0):
            startX = -1
        if (y > 0):
            startY = -1

        #Need to subtract 1 from the board width and height for this comparison, due to the grid being 0-based
        if x < boardWidth - 1:
            endX = 1
        if y < boardHeight - 1:
            endY = 1

        if debugMode == 1:
            print ' startX: ' + str(startX) + ' to endX: ' + str(endX)
            print ' startY: ' + str(startY) + ' to endY: ' + str(endY)

#        if debugMode == 1:
#            #here because of my lack of understanding of Python
#            print 'checking X range'
#            for b in range(startX, endX + 1): #needs a +1 on the endX range to include it
#                print ' value = ' + str(b)
                
#        if debugMode == 1:
#            #here because of my lack of understanding of Python
#            print 'checking Y range'
#            for b in range(startY, endY + 1): #needs a +1 on the endY range to include it
#                print ' value = ' + str(b)

        if debugMode == 1:
            print 'Starting to check the ranges for all neighbours'


        for checkY in range(y + startY, y + endY + 1):
            if debugMode ==1:
                print ' --> Row:' + str(checkY)
            for checkX in range(x + startX, x + endX + 1):
                if debugMode ==1:
                    print ' checking ' + str(checkX) + ', ' + str(checkY)
                    print 'state: ' + str(self.state[checkX][checkY])

                   #print 'checking truthy test '
                    #print (checkX == x and checkY == y)

                if (checkX == x and checkY == y):
                    if debugMode ==1:
                        print ' skipping the x, y co-ordinate start point'

                if not (checkX == x and checkY == y):
                    #if debugMode == 1:
                        #print ' checking state'
                        #print ' state :' + str(self.state[checkX][checkY])
                    if (self.state[checkX][checkY] == 1): 
                        neighbors += 1

                        if debugMode == 1:
                            print ' found a neighbour at ' + str(checkX) + ', ' + str(checkY) + '. That''s ' + str(neighbors) + ' found.'
                    print 'state: ' + str(self.state[checkX][checkY])


            if debugMode == 1:
                print 'finished checking the row'
            
        if debugMode == 1:
            print 'finished checking all the rows'
        return neighbors

    def step(self):
        # Enumerate over every element and determine its number of neighbors
        # For each cell, check all eight neighbors and turn on or off
        processingState = copy(self.state)
        for x, y in np.ndenumerate(self.state):
            #This is an additional line that I want to remove later. (Testing git commit -i hunk staging)
            if (self._numNeighbors(x, y) < 2):
                processingState[x, y] = 0

        self.state = processingState
        # This is a comment to remove, also

