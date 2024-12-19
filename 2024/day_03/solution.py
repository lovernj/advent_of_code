import re,sys
raw = open(sys.argv[1],"r").read()
soln_1 = lambda inp: sum(map(lambda x: int(x[0])*int(x[1]),re.findall(r"mul\((\d+),(\d+)\)",inp)))
soln_2 = lambda inp: soln_1(re.sub(r"(?s)don't\(\).*?(do\(\)|$)","",inp))
print(f"Problem 1: {soln_1(raw)}")
print(f"Problem 2: {soln_2(raw)}")

# regex solutions and functional programming solutions
# usually break PEP 8 but they're quite satisfying to write.

# Part 1 finds all mul(x,y) instructions, extracts x and y, 
# maps the multiplication, then sums them up.
# Part 2 finds all segments where there's a don't() and deletes them. It then
# applies part 1 to the remaining text.
# There is an edge case in part 2 where a don't() that isn't followed by a do()
# still needs cleaned up. This solution accounts for that. 