import re
from itertools import permutations

data=open("Advent13.txt").read()

happiness=dict()
people=set()

m=re.compile("(\w+).*(gain|lose) (\d+).*\s(\w+)\.")

for i in data.split("\n"):
    p = m.search(i)
    P1=p.group(1)
    P2=p.group(4)
    gain=int(p.group(3))*(2*(p.group(2)=="gain")-1)
    
    people.add(P1)
    people.add(P2)

    for i in [(P1,P2),(P2,P1)]:
        if i in happiness:
            happiness[i]+=gain
        else:
            happiness[i]=gain

#uncomment the following 4 lines for part 2
#for i in people:
#    happiness[(i,"Me")]=0
#    happiness[("Me",i)]=0
#people.add("Me")

fixedP=people.pop()
maxHappiness=0

for i in permutations(people):
    i=list(i)
    i.append(fixedP)
    
    currHappiness=happiness[(i[len(people)],i[0])]
    currHappiness+=sum(map(lambda x,y:happiness[(x,y)],i[:-1],i[1:]))
    
    maxHappiness=max(currHappiness,maxHappiness)

print maxHappiness
