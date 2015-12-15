from re import search

data=open("Advent15.txt").read().split("\n")

capacity,durability,flavor,texture,calories=[],[],[],[],[]

for i in data:
    p=search(r"(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)",i)
    capacity.append(int(p.group(1)))
    durability.append(int(p.group(2)))
    flavor.append(int(p.group(3)))
    texture.append(int(p.group(4)))
    calories.append(int(p.group(5)))

def calcScore(x,y,z,a):
    cScore,dScore,fScore,tScore=0,0,0,0
    for i in range(len(capacity)):
        m=(x,y,z,a)[i]
        cScore+=m*capacity[i]
        dScore+=m*durability[i]
        fScore+=m*flavor[i]
        tScore+=m*texture[i]
    if cScore<=0 or dScore<=0 or fScore<=0 or tScore<=0:
        return 0
    else:
        return cScore*dScore*fScore*tScore
        
maxScore=0
for x in range(0,101):
    for y in range(0,101):
        if x+y>100:
            break
        for z in range(0,101):
            a=100-(x+y+z)
            if (a<0):
                break
            if x*calories[0]+y*calories[1]+z*calories[2]+a*calories[3]==500:
                maxScore=max(maxScore, calcScore(x,y,z,a))
print maxScore
