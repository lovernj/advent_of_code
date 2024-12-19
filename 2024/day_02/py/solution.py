import sys
raw = open(sys.argv[1],'r').readlines()

# We can check basic safety by running a delta list across the values
# And then there's three conditions to check:
# 1. nothing is equal to the thing right before it
# 2. Nothing is too much bigger/smaller than the thing right before it
# 3. the max and min delta are either both positive or both negative

def is_safe(record):
    delta = [y-x for x,y in zip(record[:-1],record[1:])]
    mn,mx = min(delta), max(delta)
    if delta.count(0)>0 or abs(mn) > 3 or abs(mx) > 3 or mn*mx<0:
        return False
    return True

# I think there's probably an elegant way to identify 'problem' values
# and then check if cutting them out would solve the record
# That's not what this does. 
# Instead it just cuts out each individual value and checks if the record 
# otherwise satisfies is_safe
def is_safe_2(record):
    if is_safe(record):
        return True
    for index in range(len(record)):
        tmp = [x for idx,x in enumerate(record) if idx != index]
        if is_safe(tmp):
            return True
    return False

# Solve
safes_1, safes_2 = 0,0
for record in raw:
    clean = [int(x) for x in record.split()]
    if is_safe(clean):
        safes_1 += 1
    if is_safe_2(clean):
        safes_2 += 1
print(f"Part 1: {safes_1}")
print(f"Part 2: {safes_2}")