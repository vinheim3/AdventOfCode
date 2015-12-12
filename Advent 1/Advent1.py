data, floor=open("Advent1.txt").read(), 0

print sum(i.count("(")-i.count(")") for i in data)

for i in range(len(data)):
    floor+=2*(data[i]=='(')-1
    if floor==-1:
        print i+1
        break
