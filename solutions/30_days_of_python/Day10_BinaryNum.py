#!/bin/python3

import sys
n = int(input().strip())
binary = "{0:b}".format(n)
#print(binary)

curr_count = 0
prev_count = 0

for i in range(0,len(binary)):
    if int(binary[i]) == 1:
        #print(int(binary[i]))
        curr_count = curr_count + 1
        #print(curr_count)
    else:
        prev_count = max(curr_count, prev_count)
        curr_count = 0

print(max(prev_count, curr_count))
