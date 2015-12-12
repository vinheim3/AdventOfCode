#password="cqjxjnds"
password="cqjxxyzz"
digits=len(password)
numPass=[]

def checkPass():
    cons=False
    found=False
    doubles=0
    
    for i in range(digits):
        if numPass[i] in [105, 111, 108]:
            return False
        
        if i < digits-2:
            if numPass[i+1]-numPass[i]==1 and numPass[i+2]-numPass[i+1]==1:
                cons=True

        if i < digits-1:
            if found:
                found=False
            elif numPass[i]==numPass[i+1]:
                doubles+=1
                found=True

    return (cons and doubles>=2)

#a-97,i-105, o-111, l-108, z-122
for i in range(digits):
    numPass.append(ord(password[i]))

while True:
    for i in range(digits):
        if numPass[digits-i-1]==122:
            numPass[digits-i-1]=97
        else:
            numPass[digits-i-1]+=1
            break
        
    if checkPass():
        break

print "".join(chr(i) for i in numPass)
