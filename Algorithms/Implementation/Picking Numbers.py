#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    aa = list(set(a))
    aa = sorted(aa)
    tt = [a.count(i) for i in aa]
    p = [tt[i]+tt[i+1] for i in range(len(tt)-1) if aa[i+1]-aa[i]==1]       
    if len(tt)==1:
        return len(a)
    return max(p)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
