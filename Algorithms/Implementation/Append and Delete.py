#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    cnt = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            cnt+=1
        else:
            break
   
    t1, t2 = len(s)-cnt, len(t)-cnt

    if k>= min(t1+t2, 2*len(t)) and len(s)>=len(t):
        return 'Yes'   
    if k>= len(s)+len(t) and len(s)<len(t):
        return 'Yes'
    if k>= t1+t2 and len(s)<len(t) and t[0]==t[1]:
        return 'Yes'
    else:
        return "No"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
