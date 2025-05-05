#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    bitmask = 0
    
    for letter in s.lower():
        # check if the letter is alphabetic
        if letter.isalpha():
            # sets corresponding bit for letter
            bitmask |= 1 << (ord(letter) - ord('a'))
        
        # checks if all letters are found
        if bitmask == (1 << 26) -1:
            return('pangram')
    return('not pangram')
    
    # print(words)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
