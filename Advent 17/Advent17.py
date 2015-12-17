import itertools

data=open("Advent17.txt").read().split("\n")
count=0
found=False

for j in range(len(data)):
    if found==True:
        break
    for i in itertools.combinations(data, j):
        if sum(int(x) for x in i)==150:
            count+=1
            #found=True

print count
