from copy import deepcopy
data=open("Advent19.txt").read().split("\n")

lines=[]
strings=set()
for i in data[:-2]:
    lines.append(i.split(" => "))
string=data[-1]

for c,i in enumerate(lines):
    currStr=[]
    for d,j in enumerate(string):
        p=len(i[0])
        if d!=len(string)-(p-1) and i[0]==string[d:d+p]:
            newStr=deepcopy(currStr)
            newStr.append(i[1])
            newStr.append(string[d+p:])
            strings.add("".join(deepcopy(newStr)))
        currStr.append(j)
print len(strings)
