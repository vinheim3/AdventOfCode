with open("Advent5.txt") as myfile:
    data=myfile.read().split()

numOfGoodWords=0
for i in data:
    currentVowelCount=0
    doubleLetter=False
    badString=False
    
    for itr in range(len(i)):
        currLetter=i[itr]
        
        if currLetter in ('a', 'e', 'i', 'o', 'u'):
            currentVowelCount+=1
            
        if itr!=0:
            lastLetter=i[itr-1]
            if lastLetter==currLetter:
                doubleLetter=True
            if lastLetter+currLetter in ("ab", "cd", "pq", "xy"):
                badString=True
    
    if (currentVowelCount>=3 and doubleLetter and not badString):
        numOfGoodWords+=1

print numOfGoodWords
