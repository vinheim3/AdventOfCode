data=open("Advent8.txt").read().split("\n")

print sum(len(i)-len(eval(i)) for i in data)
print sum(2+i.count('\\')+i.count('"') for i in data)
