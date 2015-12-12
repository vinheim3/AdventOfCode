with open("Advent8.txt") as myfile:
    line=myfile.readline()
    data=[]
    while(line != ""):
        data.append(line)
        line=myfile.readline()

totalFullLetters=0
totalPrintedLetters=0

for i in data:
    skips=0
    totalFullLetters+=1

    for j in range(1,len(i)):
        if skips>0:
            skips-=1
            continue

        if i[j]=="\\":
            if i[j+1]=="x":
                totalFullLetters+=4
                totalPrintedLetters+=1
                skips=3
            else:
                totalFullLetters+=2
                totalPrintedLetters+=1
                skips=1
        elif i[j]=="\"":
            totalFullLetters+=1
            continue
        else:
            totalFullLetters+=1
            totalPrintedLetters+=1

print totalFullLetters-totalPrintedLetters
