# This file is just here to sync the input portion of the code across the two solutions
import sys,re

raw = open(sys.argv[1],'r').readlines()
input_data = [(int((matches:=re.match(r"(\d+):((?:\s\d+)+)\n",line).groups())[0]),list(map(int,matches[1].split()))) for line in raw]
