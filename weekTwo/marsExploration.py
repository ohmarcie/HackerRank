#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    num_sos = int(len(s)/3)
    # print(s, num_sos)
    
    num_changed_letters = 0
    first_s = 0
    second_o = 1
    third_s = 2
    
    for sos in range(num_sos):
        if s[first_s] != 'S':
            num_changed_letters += 1
        if s[second_o] != 'O':
            num_changed_letters += 1
        if s[third_s] != 'S':
            num_changed_letters += 1
            
        print(s[first_s], s[second_o], s[third_s])
        
        first_s += 3
        second_o += 3
        third_s += 3
    
    return num_changed_letters
    # for every letter in s
    # if first s in sos == s, pass
    # if second o in sos == o, pass
    # if third s in sos == ss, pass
    # otherwise count+= 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
