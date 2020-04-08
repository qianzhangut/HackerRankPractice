#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    s=s.split()
    s=''.join(s)
    t=[ord(i.lower()) for i in s]
    tt=list(set(t))
    if len(tt)==26:
        return 'pangram'
    return 'not pangram'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
