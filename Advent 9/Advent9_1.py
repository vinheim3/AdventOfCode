from itertools import permutations

with open("Advent9.txt") as myfile:
    data=myfile.read().split('\n')

distances={}
locations=[data[0].split()[0]]

for i in data:
    if i.split()[0]==locations[0]:
        locations.append(i.split()[2])

for i in data:
    words=i.split()
    distances[(words[0],words[2])]=words[4]
    distances[(words[2],words[0])]=words[4]

shortDist=9999
longDist=0

for routes in permutations(locations,len(locations)):
    currDist=0
    for i in range(len(locations)-1):
        currDist+=int(distances[(routes[i],routes[i+1])])

    shortDist=min(shortDist,currDist)
    longDist=max(longDist,currDist)

print shortDist
print longDist
