data=list(i.split() for i in open("Advent23.txt").read().split("\n"))

d={"a":0,"b":0}
i=0

while i<len(data):
    cI=data[i]
    #print cI
    if len(cI)==2:
        if "hlf" in cI:
            d[cI[1]]/=2
        elif "tpl" in cI:
            d[cI[1]]*=3
        elif "inc" in cI:
            d[cI[1]]+=1
        elif "jmp" in cI:
            i=eval(str(i)+cI[1])
            continue
    elif len(cI)==3:
        if "jie" in cI:
            if d[cI[1][0]]%2==0:
                i=eval(str(i)+cI[2])
                continue
        elif "jio" in cI:
            if d[cI[1][0]]==1:
                i=eval(str(i)+cI[2])
                continue
    i+=1

print d["b"]
