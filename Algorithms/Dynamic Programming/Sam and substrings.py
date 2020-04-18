#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    s=list(str(n))
    t=[int(i) for i in s]

    prev = t[0]
    res = prev
    current=0
    
    for i in range(1,len(t)):
        current=(i + 1)* t[i] + 10 * prev
        res+=current
        prev =current
    return res%1000000007

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
