#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # print(grades)
    
    new_grades = []
    for grade in grades:
        if grade < 38:
            new_grades.append(grade)
        elif grade%5 >= 3:
            print(grade%5)
            new_grades.append(grade + (5 - grade%5))
        else:
            new_grades.append(grade)
    
    # print(new_grades)
    return new_grades
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
