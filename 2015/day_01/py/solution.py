import sys

#!/usr/bin/env python3
# solution.py - Advent of Code 2015 Day 1


def part1(data: str) -> int:
    return data.count('(') - data.count(')')

def part2(data: str) -> int:
    floor = 0
    for i, ch in enumerate(data, start=1):
        if ch == '(':
            floor += 1
        elif ch == ')':
            floor -= 1
        if floor < 0:
            return i

if __name__ == "__main__":
    # Read input and preprocess
    with open(sys.argv[1], 'r') as file:
        data = file.read()
    print(f"Solution 1: {part1(data)}")
    print(f"Solution 2: {part2(data)}")