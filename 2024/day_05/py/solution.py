import re,sys
from collections import defaultdict
from functools import cmp_to_key

raw = open(sys.argv[1],'r').readlines()

# Dump the raw input into two lists so we can work with it
rules,inputs = [],[]
for line in raw:
    if tmp:=re.match(r"(\d\d)\|(\d\d)\n",line):
        rules.append((tmp[1],tmp[2]))
    elif re.match(r"(\d{2},?)+",line):
        inputs.append(line[:-1].split(','))

# Create rules 'backwards': 
# instead of X needs to be before Y, say Y needs to be after X
post_dict = defaultdict(list)
for pre,post in rules: post_dict[post].append(pre)

# To test an input line, check the sublist following each index.
# for each element in the sublist, check its post_dict to see if there's a rule
# preventing it from being there. 
def test_input(inp):
    for ind,item in enumerate(inp):
        for x in inp[:ind]:
            if item in post_dict[x]:
                return False
    return True

# It's just quicksort. Take the first item in the list (pivot)
# and sort it into pre/post depending on post_dict.
# Then run reorder on the sublists.
# I later realized that you can just use sorted() if you pass it a 
# 'spaceship operator' function. This is included because it's good code.
def reorder(inp):
    if len(inp)<2:
        return inp
    tmp = post_dict[inp[0]]
    pre = []
    post = []
    for item in inp[1:]:
        if item not in tmp:
            post.append(item)
        else:
            pre.append(item)
    return reorder(pre)+[inp[0]]+reorder(post)


get_middle = lambda x: int(x[len(x)//2])
corr_sum = incorr_sum = 0
sort_fn = lambda x,y: 1 if x in post_dict[y] else -1
for inp in inputs:
    if test_input(inp):
        corr_sum += get_middle(inp)
    else:
        incorr_sum += get_middle(sorted(inp,key=cmp_to_key(sort_fn)))

print(f"Part 1: {corr_sum}\nPart 2: {incorr_sum}")