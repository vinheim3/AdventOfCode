from itertools import product

data=list(i.split() for i in open("Advent21.txt").read().split("\n"))
a,r=[[0,0,0]],[[0,0,0],[0,0,0]]
w=list(list(int(j) for j in i[1:]) for i in data[1:6])
a.extend(list(list(int(j) for j in i[1:]) for i in data[8:13]))
r.extend(list(list(int(j) for j in i[2:]) for i in data[15:21]))

def fight(myDam, myArm):
    myHP,hisHP,hisDam,hisArm=100,104,8,1
    myTDam,hisTDam=max(myDam-hisArm,1),max(hisDam-myArm,1)
    myHits=hisHP/myTDam+(hisHP%myTDam>0)
    hisHits=myHP/hisTDam+(myHP%hisTDam>0)
    return myHits<=hisHits

minCost,maxCost=9999,0

for i in product(range(len(w)),range(len(a)),range(len(r)),range(len(r))):
    if i[2]!=i[3]:
        currCost,currDam,currArm=(sum(m[n] for m in (w[i[0]],a[i[1]],r[i[2]],r[i[3]])) for n in range(3))

        if fight(currDam, currArm):
            minCost=min(minCost,currCost)
        else:
            maxCost=max(maxCost,currCost)

print "Minimum cost to win: "+str(minCost)
print "Maximum cost to still lose: "+str(maxCost)
