import sys 

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
    print left, right

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
    print (result)
    
    return result
                        
a = [5, 4, 3, 2, 1]
mergeSort(a)
        
