import sys
import re
import time
def part1_naive(input_str: str) -> int:
    minval,maxval = map(int,input_str.split("-"))
    count = 0
    match = re.compile(r'^(\d+)\1$')
    for i in range(minval, maxval + 1):
        if match.match(str(i)):
            count += i
    return count

def harness(f, input_str) -> int:
    return sum(f(line) for line in input_str)

def part2_naive(input_str: str) -> int:
    minval,maxval = map(int,input_str.split("-"))
    count = 0
    match = re.compile(r'^(\d+)\1+$')
    for i in range(minval, maxval + 1):
        if match.match(str(i)):
            count += i
    return count

if __name__ == "__main__":
    # Read input and preprocess
    with open(sys.argv[1], 'r') as file:
        data = file.read().split(",")
    print(harness(part1_naive, data))
    print(harness(part2_naive, data))