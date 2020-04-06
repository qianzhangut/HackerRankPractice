#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year<1918 and year%4==0:
        leap='12.09.{}'.format(year) 
    elif year<1918 and year%4!=0:
        leap='13.09.{}'.format(year) 
    elif year>=1918 and year%400 ==0:
        leap = '12.09.{}'.format(year) 
    elif year>=1918 and year%4 == 0 and year%100 !=0:
        leap = '12.09.{}'.format(year) 
    elif year == 1918:
        leap = '26.09.{}'.format(year) 
    else:
        leap = '13.09.{}'.format(year)  
    return leap

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
