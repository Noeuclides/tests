#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    if len(c) == 0:
        return(0)
    count = 0
    jump = 0
    while jump < len(c):
        if jump + 2 < len(c) and c[jump + 2] == 0:
            jump = jump + 2
        else:
            jump = jump + 1
        count = count + 1
    print(count - 1)
    return(count - 1)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    #fptr.write(str(result) + '\n')

    #fptr.close()
