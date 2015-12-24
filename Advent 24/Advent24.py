from itertools import combinations
import sys

data=list(int(i) for i in open("Advent24.txt").read().split("\n"))
#part 1 is /3, part 2 is /4
perCom=sum(data)/3
found=False
minProd=sys.maxint**2

for i in range(len(data)):
    if found:
        break
    for j in combinations(data,i):
        if sum(j)==perCom:
            found=True
            minProd=min(minProd,reduce(lambda x,y:x*y,j))
            continue

print minProd
