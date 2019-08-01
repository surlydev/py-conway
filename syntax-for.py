
#Test Python syntax
x=0
y=0
startY=0
startX=0
endX=3
endY=3

for checkY in range(startY, endY):
    for checkX in range(startX, endX):
        print 'checking ' + str(x + checkX) + ' and ' + str(y + checkY) 
        if not (checkX == 1 and checkY == 1):
            print 'not 1, 1'
            print 'checked'
  
