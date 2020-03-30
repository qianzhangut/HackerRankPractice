#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos, neg, zero = 0, 0, 0
    for item in arr:
        if item>0:
            pos+=1
        elif item<0:
            neg+=1
        else:
            zero+=1
    total = pos+ neg+ zero
    return print(pos/total,'\n',neg/total,'\n',zero/total)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
