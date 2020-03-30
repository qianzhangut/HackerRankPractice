#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    tem = []
    cnt = []

    tem = list(set(arr))
    for i in tem:
        cnt.append(arr.count(i))

    t =[]
    for item in enumerate(cnt):
        if item[1] == max(cnt):
            t.append(item[0])
        
        
    return min([tem[i] for i in t])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
