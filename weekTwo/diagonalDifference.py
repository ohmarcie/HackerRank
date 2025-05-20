#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    right2left = 0
    left2right = 0
    
    # numberIndex = 0
    # numberIndex2 = len(arr) - 1
    # # print(len(arr))
    
    # for setNum in arr:
    #     for number in setNum:
    #         # print(right2left, left2right)
    #         if number == setNum[numberIndex]:
    #             right2left += number
    #         if number == setNum[numberIndex2]:
    #             left2right += number
    #     numberIndex += 1
    #     numberIndex2 -= 1
    
    # # print(right2left, left2right)
    # return abs(left2right - right2left)

    len_arr = len(arr)
    for index in range(0, len_arr):
        right2left += arr[index][index]
        left2right += arr[len_arr - index - 1][index]

    return abs(right2left - left2right)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
