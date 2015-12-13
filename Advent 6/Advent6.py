import re

data=open("Advent6.txt").read().split("\n")

lights=[]

for i in range(0,1000):
    lights.append([])
    for j in range(0,1000):
        lights[i].append(0)

m=re.compile(r"(turn on|turn off|toggle) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)")

for i in data:
    instruction,x1,y1,x2,y2=m.match(i).groups()

    #top functions are part 1, bottom functions are part 2
    if instruction=="turn on":
        function=lambda x: 1
        #function=lambda x: x+1
    elif instruction=="turn off":
        function=lambda x: 0
        #function=lambda x: max(0,x-1)
    elif instruction=="toggle":
        function=lambda x: 1-x
        #function=lambda x: x+2

    for x in range(int(x1),int(x2)+1):
        for y in range(int(y1),int(y2)+1):
            lights[x][y]=function(lights[x][y])

count=0
for i in lights:
    for j in i:
        count+=j
print count
