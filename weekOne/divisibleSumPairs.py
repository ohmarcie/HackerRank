#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    current_pos = 0
    valid_pairs = []
    num_valid = 0
    
    for value in ar:
        for index in range(n):
            if current_pos == index:
                continue
            elif (ar[index]+ar[current_pos])%k == 0:
                if valid_pairs.count([index, current_pos])>=1 or valid_pairs.count([current_pos, index])>=1:
                    continue
                else:
                    valid_pairs.append([current_pos, index])
                    valid_pairs.append([index, current_pos])
                    num_valid += 1
        current_pos += 1
    # print(valid_pairs)
    return num_valid
                
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
