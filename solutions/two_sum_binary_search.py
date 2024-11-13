#!/bin/python3

import sys
from collections import defaultdict
from math import ceil

def mergeSort(arr):
    """ Splits the array into two recursively and merges them """
    left = []
    right = []
    
    #base case
    if len(arr) <= 1:
        return arr
    
    #recursive cases
    for i in range(0,int(len(arr)/2)):
        left.append(arr[i])
     
    for j in range(int(len(arr)/2), len(arr)):
        right.append(arr[j])
        
    left = mergeSort(left)
    right = mergeSort(right)
    #print (left, right)

    return merge(left, right)

def merge(leftArr, rightArr):
    """ merges left and right Array"""
    result = []
    while len(leftArr) > 0 and len(rightArr)>0:
        if leftArr[0] < rightArr[0]:
            result.append(leftArr[0])
            leftArr.pop(0)

        else:
            result.append(rightArr[0])
            rightArr.pop(0)
    
    if len(leftArr)>0:
        result.extend(leftArr)
    
    if len(rightArr)>0:
        result.extend(rightArr)
    #print (result)
    
    return result
                        
def solve(arr, money):
    arr = mergeSort(arr)
    for i in range(len(arr)):
        key = money - arr[i]
        siblingInd = binarySearch(arr, key)
        if siblingInd >=0:
            if (siblingInd!= i or (i > 0 and arr[i-1] == arr[i]) or (i < len(arr)-1 and arr[i+1] == arr[i])):
                try:
                    print(i+1, siblingInd+1)
                except:
                    pass
                
def binarySearch(arr, element):
    print(arr)
    #base case
    mid = int(ceil(len(arr)/2))
    #print()
    print(mid,len(arr))
    if arr[mid] == element:
        return mid
    #recursive cases
    elif element > arr[mid]:
        return binarySearch(arr[mid+1:],element)
    elif element < arr[mid]:
        print(arr[0:mid-1])
        return binarySearch(arr[0:mid-1], element)    
    
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)
