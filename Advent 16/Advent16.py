from re import search

data=open("Advent16.txt").read().split("\n")
aunt={}
mySet={"children":"3","cats":"7","samoyeds":"2","pomeranians":"3","akitas":"0",
       "vizslas":"0","goldfish":"5","trees":"3","cars":"2","perfumes":"1"}

for i in data:
    p=search(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)",i).groups()

    aunt[p[0]]={p[1]:p[2],p[3]:p[4],p[5]:p[6]}

for i in aunt:
    found=True
    for j in aunt[i]:
        #the following 2 if blocks can be left out for part 1
        if j=="cats" or j=="trees":
            if aunt[i][j]<=mySet[j]:
                found=False
                break
            continue
        if j=="pomeranians" or j=="goldfish":
            if aunt[i][j]>=mySet[j]:
                found=False
                break
            continue
        if aunt[i][j]!=mySet[j]:
            found=False
            break
    if found:
        print i
        break
