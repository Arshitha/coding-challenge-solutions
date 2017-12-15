#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

i = len(arr) - 1
#print(arr[i])
revArr = []

while i >= 0:
    revArr.append(str(arr[i]))
    i = i - 1

print(' '.join(revArr))
