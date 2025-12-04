import sys

def harness(data, functions):
    """ Generic harness to run multiple functions on the same input data """
    position = [50]*len(functions)
    count = [0]*len(functions)
    for move in data:
        for i,func in enumerate(functions):
            position[i], count[i] = func(move, position[i], count[i])
    return count

def part1(move, position, count):
    position += move
    position %= 100
    return position, count + int(position==0)

def part2_naive(move, position, count):
    direction = 1 if move > 0 else -1
    while move != 0:
        position += direction
        position %= 100
        move -= direction
        if position == 0:
            count += 1
    return position, count

def part2_optimized(move, position, count):
    position += move
    if not (0<position<100):
        # An overflow has occurred.
        if position > 0:
            count += position//100
        else:
            count += abs((position-1)//100)
    return position%100, count

if __name__ == "__main__":
    # Read input and preprocess
    with open(sys.argv[1], 'r') as file:
        data = file.read().replace("L","-").replace("R","+")
        data = list(map(int,data.strip().split('\n')))
    solutions = harness(data, [part1, part2_optimized])
    print(f"Solution 1: {solutions[0]}")
    print(f"Solution 2: {solutions[1]}")