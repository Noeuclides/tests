#!/usr/bin/python3

import math
import os
import random
import re
import sys

count = 0

# Complete the minimumBribes function below.
def minimumBribes(q):
    global count
    left = 0
    right = len(q) - 1
    c = quicksort(q, left, right)
    print("minimumbribes", count)
    
def quicksort(q, left, right):
    global count
    
    if left < right:
        pivot = partition(q, left, right)
        quicksort(q, 0, pivot - 1)
        quicksort(q, pivot + 1, right)

def partition(q, left, right):
    global count
    index = left - 1
    pivot = right
    c = 0
    for i in range(left, right):
        print(i, "<" ,right)
        if q[i] < q[right]:
            index = index + 1
            q[i], q[index] = q[index], q[i]
            if index != i:
                c = c + 1
                print("c if", c)
    print("pivot {}, index + 1 {}".format(pivot, index + 1))
    q[pivot], q[index + 1] = q[index + 1], q[pivot]
    if pivot != index + 1:
        c = c + 1
    print(q)
    print("count = {} + {}".format(count, c))
    count = count + c
    print("count = ", count)
    return(index + 1)

    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
