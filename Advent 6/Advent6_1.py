with open("Advent6.txt") as myfile:
    data=[i for i in myfile]

lights=[]

for i in range(0,1000):
    lights.append([])
    for j in range(0,1000):
        lights[i].append(0)

def getNumAndDigits(string, stopper):
    digits=0
    num=""
    for i in string:
        digits+=1
        if i==stopper:
            return [int(num),digits]
        else:
            num+=i
            
for i in data:
    instruction=""
    readI=0
    currNum=""
    nums=[0,0,0,0]
    
    if i[6]=="n":
        instruction="turn on"
        readI=8
    elif i[6]=="f":
        instruction="turn off"
        readI=9
    elif i[6]==" ":
        instruction="toggle"
        readI=7

    pair=getNumAndDigits(i[readI:],",")
    nums[0]=pair[0]
    readI+=pair[1]
    
    pair=getNumAndDigits(i[readI:]," ")
    nums[1]=pair[0]
    readI+=pair[1]+8

    pair=getNumAndDigits(i[readI:],",")
    nums[2]=pair[0]
    readI+=pair[1]

    pair=getNumAndDigits(i[readI:],'\n')
    nums[3]=pair[0]
    
    if instruction=="turn on":
        function=lambda x: 1
    elif instruction=="turn off":
        function=lambda x: 0
    elif instruction=="toggle":
        function=lambda x: 1-x

    for x in range(nums[0], nums[2]+1):
        for y in range(nums[1], nums[3]+1):
            lights[x][y]=function(lights[x][y])

count=0
for i in lights:
    for j in i:
        if j==1:
            count+=1
print count
