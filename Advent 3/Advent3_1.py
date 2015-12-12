with open("Advent3.txt") as myfile:
    data=myfile.read()

currX=0
currY=0
visitedHouses={0: [0]}
numOfVisitedHouses=1

def numInArray(num, array):
    for i in array:
        if i==num:
            return True
    return False

for i in data:
    if i=='>':
        currX+=1
    elif i=='<':
        currX-=1
    elif i=='v':
        currY+=1
    elif i=='^':
        currY-=1

    if currX in visitedHouses:
        if not numInArray(currY, visitedHouses[currX]):
            visitedHouses[currX].append(currY)
            numOfVisitedHouses+=1
    else:
        visitedHouses[currX]=[currY]
        numOfVisitedHouses+=1

print numOfVisitedHouses
