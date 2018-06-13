#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict



if __name__ == '__main__':
    N = int(input())
    
    userDict = defaultdict(lambda: ' ')
    gmailIDs = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        # print(firstNameEmailID)

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        matches = re.match(r".*@gmail.com", emailID)
        userDict[emailID] = firstName
        if matches:
            gmailIDs.append(matches.group())
        else:
            continue
    
    # print(gmailIDs)
    # print(userDict)
    result = []
    for i in range(len(gmailIDs)):
        result.append(userDict[gmailIDs[i]])
        
    result = sorted(result)
        
    for ind in range(len(result)):
        print(result[ind])
        
        
    
        
