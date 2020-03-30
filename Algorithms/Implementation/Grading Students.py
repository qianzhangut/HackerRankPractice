#!/bin/python3

import math
import os
import random
import re
import sys

#
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    aa = []
    for grade in grades: # Write your code here
        if grade>=38 and grade%5 >= 3:
            grade = (grade//5+1)*5
            aa.append(grade)
        else:
            grade = grade
            aa.append(grade)
    return aa

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
