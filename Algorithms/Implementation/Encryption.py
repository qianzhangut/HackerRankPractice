#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    l = len(s)
    row = math.floor(math.sqrt(l))
    col = math.ceil(math.sqrt(l))
    if row*col<l:
        row=col
    tt = []
    a = [i for i in range(0,l,col)]
    for i in range(col): 
        c = [j+i for j in a]
        if c[-1]>=l:
            c.pop(row-1)
        b = ''.join(s[j] for j in c)
        tt.append(b)
    return tt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(' '.join(map(str, result)))


    fptr.close()
