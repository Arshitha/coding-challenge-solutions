#!/bin/python3
import sys

def MergeAndCount(LeftArr, RightArr):
    a, b, crossInvCount = 0, 0, 0
    outList = []

    while a < len(LeftArr) and b < len(RightArr):
        if LeftArr[a] > RightArr[b]:
            nextVal = RightArr[b]
            #RightArr.pop(b)
            b+=1
            crossInvCount += len(LeftArr) - a

        elif LeftArr[a] <= RightArr[b]:
            nextVal = LeftArr[a]
            a+=1
            #LeftArr.pop(a)
        
        outList.append(nextVal)
        
    if len(LeftArr) > 0:
        outList.extend(LeftArr[a:])
    
    if len(RightArr)>0:
        outList.extend(RightArr[b:])

    return crossInvCount, outList

def countInversions(arr):
    if len(arr) == 1 or len(arr)==0:
        return 0, arr
    
    midpoint = int(len(arr)/2)
    A = arr[:midpoint]
    B = arr[midpoint:]

    invA, sortedA = countInversions(A)
    invB, sortedB = countInversions(B)
        
    crossInv, sortedList = MergeAndCount(sortedA, sortedB)

    return invA + invB + crossInv, sortedList

            
if __name__ == "__main__":
    global invCount
    t = int(input().strip())
    for a0 in range(t):
        invCount = 0
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result[0])
