w=[[8,4,0],[10,5,0],[25,6,0],[40,7,0],[74,8,0]]

a=[[0,0,0],[13,0,1],[31,0,2],[53,0,3],[75,0,4],[102,0,5]]

r=[[0,0,0],[0,0,0],
   [25,1,0],[50,2,0],[100,3,0],
   [20,0,1],[40,0,2],[80,0,3]]

def fight(myDam, myArm):
    turn=1
    myHP=100
    hisHP=104
    hisDam=8
    hisArm=1
    
    while True:
        if turn==1:
            hisHP-=max(myDam-hisArm,1)
        elif turn==0:
            myHP-=max(hisDam-myArm,1)
        turn=1-turn
        if min(hisHP,myHP)<=0:
            return hisHP<=0

minCost=9999
maxCost=0

for i in range(len(w)):
    for j in range(len(a)):
        for k in range(len(r)):
            for l in range(len(r)):
                if k!=l:
                    currCost=w[i][0]+a[j][0]+r[k][0]+r[l][0]
                    currDam=w[i][1]+r[k][1]+r[l][1]
                    currArm=a[j][2]+r[k][2]+r[l][2]
                    
                    if fight(currDam, currArm):
                        minCost=min(minCost,currCost)
                    else:
                        maxCost=max(maxCost,currCost)

print minCost
print maxCost
