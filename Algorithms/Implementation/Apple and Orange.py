#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    app = [a+i for i in apples]
    ora = [b+j for j in oranges]
    count1 = [i for i in app if (i>=s and i<=t)]
    count2 = [i for i in ora if (i>=s and i<=t)] 
    return len(count1), len(count2)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    a1, a2 = countApplesAndOranges(s, t, a, b, apples, oranges)
    print(a1)
    print(a2)
