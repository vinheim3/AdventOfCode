import re, json

data=open("Advent12.txt").read()

def deleteRed(items):
    if type(items) is dict:
        if "red" in items.values():
            items.clear()
            return items
        for i in items.items():
            items[i[0]]=deleteRed(i[1])
    elif type(items) is list:
        for i in items:
            deleteRed(i)
    return items

#uncomment the following 3 lines for part 2
#data=json.loads(data)
#data=deleteRed(data)
#data=json.dumps(data)

print sum(int(i) for i in (re.findall(r'-?\d+', data)))
