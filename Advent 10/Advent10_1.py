data="1321131112"

#range(40) for part 1, range(50) for part 2
#cL-current letter
#cS-current string
#cLC-current letter count
for j in range(50):
    cL=data[0]
    cS=""
    cLC=1
    for i in range(1,len(data)):
        if data[i]==cL:
            cLC+=1
        else:
            cS+=str(cLC)+cL
            cL=data[i]
            cLC=1
    cS+=str(cLC)+cL
    data=cS
print len(data)
