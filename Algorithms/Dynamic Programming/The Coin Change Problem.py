#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    
 
    # Create the ways array to 1 plus the amount 
    # to stop overflow 
    ways = [0] * (n + 1); 
  
    # Set the first way to 1 because its 0 and 
    # there is 1 way to make 0 with 0 coins 
    ways[0] = 1; 
  
    # Go through all of the coins 
    for i in range(len(c)): 
  
        # Make a comparison to each index value 
        # of ways with the coin value. 
        for j in range(len(ways)): 
            if (c[i] <= j): 
  
                # Update the ways array 
                ways[j] += ways[(int)(j - c[i])]; 
  
    # return the value at the Nth position 
    # of the ways array. 
    return ways[n]; 
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
