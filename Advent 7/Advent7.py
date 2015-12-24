data=open("Advent7.txt").read().split("\n")

lines=[]

for i in data:
    lines.append([])
    lines[len(lines)-1]=i.split()

#lines.append(["19138","->","b"])
lines.append(["16076","->","b"])

while True:
    solved={}
    toDelete=[]
    
    for c,i in enumerate(lines):
        oldSolved=len(solved)
        if len(i)==3 and i[0].isdigit():
            solved[i[2]]=i[0]
        elif len(i)==4 and i[1].isdigit():
            solved[i[3]]=str(65536+~int(i[1]))
        elif len(i)==5 and i[0].isdigit() and i[2].isdigit():
            if i[1]=="AND":
                solved[i[4]]=str(int(i[0])&int(i[2]))
            elif i[1]=="OR":
                solved[i[4]]=str(int(i[0])|int(i[2]))
            elif i[1]=="LSHIFT":
                solved[i[4]]=str(int(i[0])<<int(i[2]))
            elif i[1]=="RSHIFT":
                solved[i[4]]=str(int(i[0])>>int(i[2]))
        if len(solved)>oldSolved:
            toDelete.append(c)

    if "a" in solved:
        print solved["a"]
        break
    
    while len(toDelete)>0:
        i=toDelete.pop()
        del lines[i]
    
    for a,i in enumerate(lines):
        for b,j in enumerate(i):
            if j in solved:
                lines[a][b]=solved[j]
