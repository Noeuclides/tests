#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hg = 0
    row = 0
    column = 0
    sum = 0
    hourglass = -63
    while hg < 16:
        for r in range(row, row + 3):
            for c in range(column, column + 3):
                if not (r == row + 1 and (c == column or c == column + 2)):
                    sum = sum + arr[r][c]
        column = column + 1
        if column == 4:
             row = row + 1
             column = 0
        hg = hg + 1
        if abs(sum) > hourglass:
            hourglass = sum
        sum = 0

    print(hourglass)
    return(hourglass)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()
