#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    neg = []
    zero = []
    pos = []
    
    for i in arr:
        if i>0:
            pos.append(i)
        if i==0:
            zero.append(i)
        if i<0:
            neg.append(i)
        
    print(len(pos)/len(arr))
    print(len(neg)/len(arr))
    print(len(zero)/len(arr))    
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
