#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(B):
    s0=s1=0
    for i in range(1,len(B)):
        tmp=s0
        s0=max(s0,s1+abs(B[i-1]-1))
        s1=max(s1+abs(B[i]-B[i-1]),tmp+abs(B[i]-1))
    return max(s0,s1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
