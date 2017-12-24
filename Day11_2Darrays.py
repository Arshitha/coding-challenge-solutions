#!/bin/python3

import sys


arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

sumList = []
for i in range(6):
    for j in range(6):
        if i+1 < 6 and i+2<6 and j+1<6 and j+2<6:
            hourglassSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            sumList.append(hourglassSum)
        else: 
            pass

max = 0 
for each in sumList:
    if max < each:
        max = each
print(max)
