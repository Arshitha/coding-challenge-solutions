#!/bin/python3

import sys
from math import ceil

def workbook(n, k, arr):
    spProb = 0; page = 0; 
    currPage = 1
    #loops through all of the chapters
    for chap in range(n):
        pr = arr[chap]
        pagesReq = int(ceil(pr/k))
        
        #iterates through every problem and increments the current page number and special problem count
        while (currPage >= page) and (currPage <=page+pagesReq):
            for i in range(1, pr+1):
                if i==currPage:
                    spProb +=1
                if (i%k == 0) or i==pr:
                    currPage+=1
        page +=pagesReq

    return spProb
    

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = workbook(n, k, arr)
    print(result)
