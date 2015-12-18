import copy
data=open("Advent18.txt").read().split("\n")

lights=[]
for a,i in enumerate(data):
    lights.append([])
    for j in i:
        lights[a].append(j=='#')
newList=copy.deepcopy(lights)

def calcNeighbours(x, y):
    neigh=sum(((0 <= i < 100) and (0 <= j < 100) and lights[i][j])
              for i in range(x-1,x+2) for j in range(y-1,y+2) if (i,j)!=(x,y))

    return ((lights[x][y] and neigh==2) or neigh==3)

for i in range(100):
    for x in range(100):
        for y in range(100):
            newList[x][y]=calcNeighbours(x, y)
            
    lights=copy.deepcopy(newList)

    #uncomment the following for part 2
    #lights[0][0],lights[0][99],lights[99][0],lights[99][99]=1,1,1,1
    
print sum(sum(i) for i in lights)
