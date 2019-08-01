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
            print 'x=' + str(x) + ' y=' + str(y)
        startX = 0
        startY = 0
        endX = 0
        endY = 0
        neighbors = 0
        boardWidth = self.board_size[0]
        boardHeight = self.board_size[1]

        if (x > 0):
            startX = -1
        if (y > 0):
            startY = -1

        if x < boardWidth:
            endX = 1
        if y < boardHeight:
            endY = 1

        if debugMode == 1:
            print ' x: ' + str(x) + ' y: ' + str(y)
            print ' startX: ' + str(startX) + ' endX: ' + str(endX)
            print ' startY: ' + str(startY) + ' endY: ' + str(endY)

        if debugMode == 1:
            print 'checking X range'
            for b in range(startX, endX + 1): #needs a +1 on the endX range to include it
                print ' value = ' + str(b)
                
        if debugMode == 1:
            print 'checking Y range'
            for b in range(startY, endY + 1): #needs a +1 on the endY range to include it
                print ' value = ' + str(b)

        for checkY in range(startY, endY + 1):
            for checkX in range(startX, endX + 1):
                if debugMode ==1:
                    print ' checking ' + str(x + checkX) + ' and ' + str(y + checkY)
                if not (checkX == 0 and checkY == 0):
                    if debugMode == 1:
                        print ' state :' 
                        print self.state[x + checkX][y + checkY]
                    if (self.state[x + checkX][y + checkY] == 1): 
                        neighbors += 1
                        if debugMode == 1:
                            print ' found a neighbour at ' + str(x + checkX) + ', ' + str(y + checkY) + '. That''s ' + str(neighbors) + ' found.'


        return neighbors

    def step(self):
        # Enumerate over every element and determine its number of neighbors
        # For each cell, check all eight neighbors and turn on or off
        processingState = copy(self.state)
        for x, y in np.ndenumerate(self.state):
            if (self._numNeighbors(x, y) < 2):
                processingState[x, y] = 0

        self.state = processingState
