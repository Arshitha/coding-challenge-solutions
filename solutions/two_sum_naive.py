#!/bin/python3

import sys

def solve(arr, money):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if costTable[i+1] + costTable[j+1] == money:
                print(i+1, j+1)
    

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)
