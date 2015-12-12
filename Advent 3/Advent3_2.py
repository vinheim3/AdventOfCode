with open("Advent3.txt") as myfile:
    data=myfile.read()

#1st 0 is turn-santa is 0, robo is 1
#next 2 0s is santa's x and y
#next 2 0s is robo's x and y
turnCoords=[0,0,0,0,0]
visitedHouses={0: [0]}

numOfVisitedHouses=1

def numInArray(num, array):
    for i in array:
        if i==num:
            return True
    return False

def visit(xVal, yVal):
    if xVal in visitedHouses:
        if not numInArray(yVal, visitedHouses[xVal]):
            visitedHouses[xVal].append(yVal)
            return 1
    else:
        visitedHouses[xVal]=[yVal]
        return 1
    return 0

for i in data:
    arrayX=turnCoords[0]*2+1
    arrayY=turnCoords[0]*2+2
    if i=='>':
        turnCoords[arrayX]+=1
    elif i=='<':
        turnCoords[arrayX]-=1
    elif i=='v':
        turnCoords[arrayY]+=1
    elif i=='^':
        turnCoords[arrayY]-=1

    numOfVisitedHouses+=visit(turnCoords[arrayX], turnCoords[arrayY])
    turnCoords[0]=1-turnCoords[0]

print numOfVisitedHouses
