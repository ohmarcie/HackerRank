#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # print(scores)
    
    list_score = []
    for score in scores:
        list_score.append(score)
    
    num_min = 0
    num_max = 0
    min = list_score[0]
    max = list_score[0]
    for i in list_score:
        if i < min:
            num_min +=1
            min = i
        if i > max:
            num_max +=1
            max = i
    return(num_max, num_min)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
