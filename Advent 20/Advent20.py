data=34000000
pph=10 #presents per house, part 1=10, part 2=11
tData=data/pph+(data%pph>0)

#first is part 1, second is part 2
stopCond=lambda x:tData+1
#stopCond=lambda x:min(x*50,tData)+1

house=[0]
for i in range(tData):
    house.append(0)
    
for i in range(1, tData+1):
    for j in range(i, stopCond(i), i):
        house[j]+=i

for i in range(1, tData+1):
    if house[i]>tData:
        print i
        break
