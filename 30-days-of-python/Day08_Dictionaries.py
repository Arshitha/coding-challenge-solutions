#!/usr/bin/python
import sys

phoneDict = {}
n = int(input())
#print(n)

while(n>0):
    #print("here")
    inp = input().split()
    phoneDict[str(inp[0])] = inp[1]
    n = n - 1

for each in sys.stdin:
    each = each.replace("\n","")
    if each in phoneDict:
        print("%s=%s" %(each, phoneDict[each]))
    else:
        print("Not found")
