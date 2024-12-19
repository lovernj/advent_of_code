from get_input import input_data

# Both of the parts down below rely on the fact that addition, multiplication, 
# and concatenation are closed over the natural numbers but their inverse operations
# are not.

# One way to check if a set of ops solve a line is to iteratively un-apply the operations
# until you get to the end, and if the resulting value makes sense, then the ops probably
# solved the equation.

# We can short-circuit this pretty heavily. 
# If an operation would produce an invalid state:
# - The intermediate value is not divisible by an input means that dividing by it 
#    would produce a noninteger
# - The intermediate value is less than an input means that subtracting by it 
#    would produce a value less than zero
# - The intermediate value does not end with the input means that the input
#   could not have been concatenated to the intermediate value

# From here, we can recurse down the tree of ops until we find a winning combo

#Part 1
def check_input(output,inputs):
    if len(inputs)==1:
        return output==inputs[0]
    return ((output > inputs[-1] and check_input(output-inputs[-1],inputs[:-1]))
           or (output%inputs[-1]==0 and check_input(output//inputs[-1],inputs[:-1])))

#Part 2
def attempt_deconcat(output,inputs,f):
    tmpo,tmpi = str(output), str(inputs[-1])
    if tmpo==tmpi:
        return len(inputs)==1
    return f(int(tmpo[:-len(tmpi)]),inputs[:-1])

def check_input_2(output,inputs):
    if len(inputs)==1:
        return output==inputs[0]
    return ((output%inputs[-1]==0 and check_input_2(output//inputs[-1],inputs[:-1])) 
            or (output > inputs[-1] and check_input_2(output-inputs[-1],inputs[:-1])) 
            or (str(output).endswith(str(inputs[-1])) and attempt_deconcat(output,inputs,check_input_2)))

# Solve
part1=part2=0
for output,inputs in input_data:
    if check_input(output,inputs):
        part1 += output
    if check_input_2(output,inputs):
        part2 += output
print(f"Part 1: {part1}\nPart 2: {part2}")