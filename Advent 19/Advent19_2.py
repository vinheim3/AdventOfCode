from re import findall
data=open("Advent19.txt").read().split("\n")[-1]
p=len(findall("[A-Z]",data))
q, r=data.count("Rn"), data.count("Y")
print p-2*(q+r)-1
