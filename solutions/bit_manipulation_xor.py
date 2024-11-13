#!/bin/python3

import sys

def lonely_integer(a):
    #a=mergeSort(a)
    value = 0
    for i in range(len(a)):
        value ^= a[i]
    return value
    
n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
