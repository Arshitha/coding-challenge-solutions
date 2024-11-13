numList = [2, 1, 3, 1, 2]

def MergeAndCount(LeftArr, RightArr):
    a, b, crossInvCount = 0, 0, 0
    outList = []

    while a < len(LeftArr) and b < len(RightArr):
        #print(len(LeftArr), len(RightArr), a, b)
        if LeftArr[a] > RightArr[b]:
            nextVal = RightArr[b]
            RightArr.pop(b)
            crossInvCount += len(LeftArr) - a

        elif LeftArr[a] <= RightArr[b]:
            nextVal = LeftArr[a]
            LeftArr.pop(a)
            #a += 1
            
        #print(nextVal, "here")
        outList.append(nextVal)
        
        #print(a, b)
        
    if len(LeftArr) > 0:
        outList.extend(LeftArr)
    
    if len(RightArr)>0:
        outList.extend(RightArr)
    
    #print (crossInvCount, outList)
    return crossInvCount, outList

def CountAndSort(arr):
    if len(arr) == 1:
        #print ("here")
        #print (0, arr)
        return 0, arr
    else:
        midpoint = int(len(arr)/2)
        A = arr[:midpoint]
        B = arr[midpoint:]
        #print (A, B)

        invA, sortedA = CountAndSort(A)
        invB, sortedB = CountAndSort(B)
        #print (invA, sortedA, invB, sortedB)

        crossInv, sortedArr = MergeAndCount(sortedA, sortedB)
    
    return invA + invB + crossInv, sortedArr



print ( CountAndSort(numList)[0] )
    
