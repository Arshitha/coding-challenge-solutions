#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int,input().strip().split(' ')))

totalSwaps = 0
for i in range(0,len(a)):
    numSwaps = 0
    
    for j in range(0, len(a)-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            totalSwaps = totalSwaps + 1
            numSwaps = numSwaps + 1
        
    if numSwaps == 0:
        break;

print("Array is sorted in %d swaps." % (totalSwaps))
print("First Element: %d" % (a[0]))
print("Last Element: %d" % (a[n-1]))
