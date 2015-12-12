import re

print sum(int(i) for i in (re.findall(r'-?\d+', open("Advent12.txt").read())))
