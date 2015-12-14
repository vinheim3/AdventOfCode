from itertools import permutations

data=open("Advent9.txt").read().split('\n')

distances={}
locations=set()

for i in data:
    loc1,_,loc2,_,distance=i.split()
    distances[(loc1,loc2)]=int(distance)
    distances[(loc2,loc1)]=int(distance)
    locations.add(loc1)
    locations.add(loc2)

shortDist=9999
longDist=0

for routes in permutations(locations,len(locations)):
    currDist=sum(map(lambda x,y:distances[(x,y)],routes[:-1],routes[1:]))    shortDist=min(shortDist,currDist)
    longDist=max(longDist,currDist)

print shortDist
print longDist
