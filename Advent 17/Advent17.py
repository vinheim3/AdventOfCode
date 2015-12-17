import itertools

data=open("Advent17.txt").read().split("\n")
count=0
mini=0

#for part 2, uncomment everything and comment out count+=1 before mini=j
for j in range(len(data)):
    for i in itertools.combinations(data, j):
        if sum(int(x) for x in i)==150:
            count+=1
            #mini=j
            #break
    if mini>0:
        break

#for i in itertools.combinations(data, mini):
#    if sum(int(x) for x in i)==150:
#        count+=1

print count
