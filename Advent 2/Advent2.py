totalsqft, totalRibbon=0, 0

for i in open("Advent2.txt"):
    l, w, h = [int(j) for j in i.split('x')]
    totalsqft += 2*(l*w+l*h+w*h)+min(l*w,l*h,w*h)
    totalRibbon += 2*min(l+w,l+h,w+h) + l*w*h
    
print totalsqft
print totalRibbon
