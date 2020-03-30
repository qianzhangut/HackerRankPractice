#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    aa = 0
    if 'PM' in s and s[:2] == '12':
        aa = '12'+ s[2:8]
    elif 'AM' in s and s[:2] == '12':
        aa = '00'+ s[2:8]
    elif 'PM' in s and  s[:2] != '12':
        aa = str(int(s[:2])+12)+s[2:8]
    else:
        aa = s[:8]
    return aa

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
