#!/bin/python3

import sys
from collections import defaultdict

def solve(arr, money):
    costTable = defaultdict(int)
    for i in range(len(arr)):
        costTable[arr[i]] +=1

    for i in range(len(arr)):
        if arr[i] != "0":
            key = money - arr[i]
            costTable[arr[i]] -= 1
            arr[i] = "0"
        if (key in costTable) and (costTable[key] !=0):
            costTable[key] -= 1
            try:
                print(i+1, arr.index(key)+1)
            except:
                pass
    
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)
