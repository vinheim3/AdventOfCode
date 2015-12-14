from re import search

data=open("Advent14.txt").read().split("\n")

seconds, nums, points, times, distance = 2503, [], [], [], []

for c,i in enumerate(data):
    nums.append([])
    nums[c]=search("(\d+).+?(\d+).+?(\d+)",i).groups()
    
    points.append(0)
    times.append([0,int(nums[c][1]),0])
    distance.append(0)

for i in range(seconds):
    for i in range(len(data)):
        timeType=times[i][0]+1
        if times[i][timeType]>0:
            times[i][timeType]-=1

            if timeType==1:
                distance[i]+=int(nums[i][0])

            if times[i][timeType]==0:
                times[i][0]=1-times[i][0]
                times[i][3-timeType]=int(nums[i][3-timeType])
    
    maxD=max(distance)
    for i in range(len(data)):
        if distance[i]==maxD:
            points[i]+=1

print max(distance)
print max(points)
