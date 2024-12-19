import sys,itertools,functools,operator
raw = open(sys.argv[1],"r").readlines()
input_data = [map(int,x.split()) for x in raw]

part1 = part2 = 0
for package in input_data:
    areas = tuple(map(lambda x: x[0]*x[1],itertools.combinations(package,2)))
    perimeters = tuple(map(lambda x: 2*(x[0]+x[1]),itertools.combinations(package,2)))
    volume = functools.reduce(operator.mul,package)
    part1 += 2*sum(areas)+min(areas)
    part2 += min(perimeters)+volume
print(f'Part 1: {part1}\nPart 2: {part2}')