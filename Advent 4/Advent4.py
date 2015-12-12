import hashlib

with open("Advent4.txt") as myfile:
    data=myfile.read()

i=0
while True:
    string="ckczppom{0}".format(i)
    m = hashlib.md5()
    m.update(string)
    i+=1

    if m.hexdigest()[:5]=="00000":
        print i
        break
