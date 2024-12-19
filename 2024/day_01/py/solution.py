import sys
raw = open(sys.argv[1],"r").readlines()


in1,in2 = [],[]
for line in raw:
    a,b = map(int,line.split())
    in1.append(a)
    in2.append(b)
in1.sort()
in2.sort()

# solve part 1
tmp = 0
for a,b in zip(in1,in2):
    tmp += abs(b-a)
print(f"Solution 1: {tmp}")

# solve part 2
tmp = 0
for a in in1:
    tmp += a*in2.count(a)
print(f"Solution 2: {tmp}")