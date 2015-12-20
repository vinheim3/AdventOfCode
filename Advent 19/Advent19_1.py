import copy
data=open("Advent19.txt").read().split("\n")

lines=[]
strings=set()
for i in data[:-2]:
    lines.append(i.split(" => "))
string=data[-1]

for c,i in enumerate(lines):
    currStr=[]
    for d,j in enumerate(string):
        if len(i[0])==1:
            if i[0]==j:
                newStr=copy.deepcopy(currStr)
                newStr.append(i[1])
                newStr.append(string[d+1:])
                strings.add("".join(copy.deepcopy(newStr)))
        elif len(i[0])==2 and d!=len(string)-1:
            if i[0]==string[d]+string[d+1]:
                newStr=copy.deepcopy(currStr)
                newStr.append(i[1])
                newStr.append(string[d+2:])
                strings.add("".join(copy.deepcopy(newStr)))
        currStr.append(j)
print len(strings)
