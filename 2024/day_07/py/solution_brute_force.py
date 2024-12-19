import itertools,functools
from get_input import input_data

# Basic operations
add = lambda x,y: x+y
mul = lambda x,y: x*y
cat = lambda x,y: int(str(x)+str(y))

# Attempt every possible set of operations on the input
# to check if it equals the output
# Do this by pairing up input elements and operations, then reducing down
# using the operation definitions found above.
# Efficiency: any() can take an iterator as input (instead of e.g. a list)
# and will short-circuit as soon as something returns true.
def test_pair (out,inp,ops):
    return any(out==functools.reduce(lambda x,y: y[1](x,y[0]), 
                                   zip(inp[1:],opset), inputs[0])
               for opset in itertools.product(ops,repeat=len(inp)-1))

# Solve
part1 = part2 = 0
for output,inputs in input_data:
    if test_pair(output,inputs,[add,mul]):     part1 += output
    if test_pair(output,inputs,[add,mul,cat]): part2 += output

print(f"Part 1: {part1}\nPart 2: {part2}")