#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # print(arr)
    
    sum = 0
    
    # add all the nums
    for i in arr:
        sum += i
        
    min_sum = sum - arr[0]
    max_sum = 0
    
    # find the min/max
    for x in arr:
        new_sum = sum - x
        if new_sum < min_sum:
            min_sum = new_sum
        if new_sum > max_sum:
            max_sum = new_sum
        new_sum = 0
    
    print(min_sum, max_sum)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
