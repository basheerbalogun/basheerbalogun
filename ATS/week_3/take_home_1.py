# Use a list to solve the following problem: Read in 20 numbers. As each number is read, print
# it only if it is not a duplicate of a number already read.
import random 

empty_list = []

for i in sorted(set(range(1,21))):
    empty_list.append(i)
print(empty_list)