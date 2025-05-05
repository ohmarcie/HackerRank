#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # print(strings, queries)
    
    results = []
    result_instance = 0
    for values2 in queries:
        for values1 in strings:
            if values1==values2:
                result_instance += 1
        results.append(result_instance)
        result_instance = 0
    
    # set1 = []
    # set2 = []
    # for values1 in strings:
    #     set1.append(values1.lower())
    # for values2 in queries:
    #     set2.append(values2.lower())
        
    # results = ''
    # result_instance = 0
    # for num_values in set2:
    #     # if set1.count(num_values) >= 1:
    #     result_instance = set1.count(num_values)
    #     results += str(result_instance) 
    #     # if result_instance == 0:
    #     #     results += '0'
    #     # results += ' '
    #     # print(result_instance)
    
    return(results)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
