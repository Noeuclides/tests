#!/usr/bin/python3

a= 'dabbcbacd'
a_set = list(set(a))
l = len(a_set)

while l <= len(a):
    print(l)
    for i in range(len(a)):
        if sorted(list(a[i:l+i])) == sorted(a_set):
            print("IF",len(a[i:l+1]), a[i:l+1])
    l = l + 1
        
