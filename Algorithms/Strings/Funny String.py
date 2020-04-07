#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    diff = [abs(ord(i)-ord(j)) for i, j in zip(s,s[1:])]
    return 'Funny' if diff==diff[::-1] else 'Not Funny'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
