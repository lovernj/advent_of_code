import sys
raw = open(sys.argv[1],'r').readlines()

# Part 1
win_list = ('XMAS','SAMX')
count = 0
for x, sublist in enumerate(raw):
    for y,elem in enumerate(sublist):
        #Only words starting with X or S will ever 'win'
        if elem in 'MA':
            continue
        # Solve horizontals
        if raw[x][y:y+4] in win_list:
            count += 1
        # Solve verticals
        if ''.join([n[y] for n in raw[x:x+4]]) in win_list:
            count += 1
        if x<= 137:
            if  y <= 137 and ''.join([n[y+m] for m,n in enumerate(raw[x:x+4])]) in win_list:
                count += 1
            if y>=3  and ''.join([n[y-m] for m,n in enumerate(raw[x:x+4])]) in win_list:
                count += 1
print(f"Part 1 solution: {count}")

# Part 2
count = 0
win_list = ('SAM','MAS')
for x,sublist in enumerate(raw):
    for y,elem in enumerate(sublist):
        if not (elem=='A' and 0<x<139 and 0<y<139):
            continue
        diag_1 = ''.join([n[y+m-1] for m,n in enumerate(raw[x-1:x+2])])
        diag_2 = ''.join([n[y-m+1] for m,n in enumerate(raw[x-1:x+2])])
        if diag_1 in win_list and diag_2 in win_list:
            count += 1
print(f"Part 2 solution: {count}")   

# Really not an elegant solution here. Both parts just brute-force check every 
# index in the grid to see if it corresponds to the listed conditions. 
# Slight speedup from checking 'impossibility' conditions and from checking
# backwars words (samx instead of xmas). 