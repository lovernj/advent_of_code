import sys
import itertools
def exhaustive(input_str: str,l) -> int:
    # Generate all combinations of l different indices
    # and find the maximum l-digit number that can be formed
    maxi = "0"
    for i in itertools.combinations(range(len(input_str)), l):
        tmp = list(i)
        tmp.sort()
        val = ''.join(input_str[j] for j in tmp)
        if val > maxi:
            maxi = val
    return maxi

def smart(input_str: str,l) -> int:
    if l<=1:
        return max(input_str)
    else:
        k = max(input_str[:-l+1])
        return k + smart(input_str[input_str.find(k)+1:],l-1)

def harness(f,l,inputs) -> int:
    # Apply function f to each line in inputs and sum the results
    return sum(int(f(line.strip(),l)) for line in inputs)

if __name__ == "__main__":
    # Read input and preprocess
    with open(sys.argv[1], 'r') as file:
        data = file.readlines()
    print(harness(smart,2,data))
    print(harness(smart,12,data))