#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countArray function below.
def countArray(n, k, x):
    a0=0 if x>1 else 1
    b0=1 if x>1 else 0 
    i=1
    while i<n:
      a, b = b0, a0*(k-1)+b0*(k-2)
      b0, a0 = b, a    
      i+=1
    return a%1000000007
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
