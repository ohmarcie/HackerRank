#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # return(s)
    times = []
    string = ''
    
    for i in s:
        if i == ':':
            times.append(string)
            string = ''
        if i == 'M' or i == 'm':
            string += i
            times.append(string)
            string = ''
        else:
            string += i
    
    string_2 = ''
    time_hr = ''
    count = 0
    for y in times[2]:
        if count <= 2:
            string_2 += y
        if count>2:
            time_hr += y
        count += 1
    times[2] = string_2
    
    if time_hr == 'AM' or time_hr == 'am':
        # new_hour = int(times[0]) + 12
        # if new_hour == 12:
        if int(times[0]) == 12:
            new_hour = '00'
            times[0] = str(new_hour)
            
    if time_hr == 'PM' or time_hr == 'pm':
        new_hour = int(times[0]) + 12
        if new_hour == 24:
            new_hour = '12'
        times[0] = str(new_hour)
    # print(times)
    
    return(times[0] + times[1] + times[2])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
