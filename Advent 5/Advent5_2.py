with open("Advent5.txt") as myfile:
    line=myfile.readline()
    data=[]
    while(line!=""):
        data.append(line)
        line=myfile.readline()

numOfGoodWords=0
letterInBetweenPair=False
duplicatePairs=False
pairArray=[]

def pairExists(pair, array):
    for i in range(0,len(array)-1):
        if pair==array[i]:
            return True
    return False

for i in data:
    for itr in range(1, len(i)):
        currPair=i[itr-1]+i[itr]
        if itr==1:
            pairArray=[currPair]
        else:
            if (i[itr-2]==i[itr]):
                letterInBetweenPair=True
            
            if pairExists(currPair, pairArray):
                duplicatePairs=True
            else:
                pairArray.append(currPair)
    
    if (letterInBetweenPair and duplicatePairs):
        numOfGoodWords+=1

    letterInBetweenPair=False
    duplicatePairs=False

print numOfGoodWords
