from re import findall

data=open("Advent5.txt").read().split()

goodWords1, goodWords2 = 0, 0

for i in data:
    currentVowelCount=len(findall(r"([aeiou])",i))
    doubleLetter=len(findall(r"(.)\1",i))
    badString=len(findall(r"ab|cd|pq|xy",i))

    inBetween=len(findall(r"([a-z]).\1",i))
    doublePairs=len(findall(r"([a-z][a-z]).*\1",i))

    if (currentVowelCount>=3 and doubleLetter and not badString):
        goodWords1+=1
        
    if (inBetween and doublePairs):
        goodWords2+=1
    
print goodWords1
print goodWords2
