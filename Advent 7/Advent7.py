with open("Advent7_2.txt") as myfile:
    data=[i.split('\n')[0] for i in myfile]

dataDict={}
for line in data:
    cmd,gate=line.split(" -> ")
    dataDict[gate]=cmd

solved={}
def get_value(key):
    if key.isdigit():
        return int(key)
    elif key in solved:
        return solved[key]

    cmd=dataDict[key].split(" ")

    if "NOT" in cmd:
        if cmd[1].isdigit() or (cmd[1] in solved):
            solved[key]=~get_value(cmd[1])
            return solved[key]
        return ~get_value(cmd[1])
    if "AND" in cmd:
        if (cmd[0].isdigit() or cmd[0] in solved) and (cmd[2].isdigit() or cmd[2] in solved):
            solved[key]=get_value(cmd[0]) & get_value(cmd[2])
            return solved[key]
        return get_value(cmd[0]) & get_value(cmd[2])
    if "OR" in cmd:
        if (cmd[0].isdigit() or cmd[0] in solved) and (cmd[2].isdigit() or cmd[2] in solved):
            solved[key]=get_value(cmd[0]) | get_value(cmd[2])
            return solved[key]
        return get_value(cmd[0]) | get_value(cmd[2])
    if "LSHIFT" in cmd:
        if (cmd[0].isdigit() or cmd[0] in solved) and (cmd[2].isdigit() or cmd[2] in solved):
            solved[key]=get_value(cmd[0]) << get_value(cmd[2])
            return solved[key]
        return get_value(cmd[0]) << get_value(cmd[2])
    if "RSHIFT" in cmd:
        if (cmd[0].isdigit() or cmd[0] in solved) and (cmd[2].isdigit() or cmd[2] in solved):
            solved[key]=get_value(cmd[0]) >> get_value(cmd[2])
            return solved[key]
        return get_value(cmd[0]) >> get_value(cmd[2])
    solved[key]=get_value(cmd[0])
    return solved[key]
print get_value("a")
