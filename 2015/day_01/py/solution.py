import sys
raw = open(sys.argv[1],'r').readlines()[0]

print(f"Part 1: {raw.count('(')-raw.count(')')}")

floor = 0
ind = 0
while floor >= 0:
    if raw[ind]=='(': floor += 1
    elif raw[ind]==')': floor -= 1
    ind += 1
print(f"Part 2: {ind}")