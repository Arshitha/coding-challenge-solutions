import sys
from itertools import combinations
from collections import defaultdict

def ransom_note(magazine, ransom):
    count = 0
    magDictionary = defaultdict(int)
    ransDictionary = defaultdict(int)
    
    for key in magazine:
        magDictionary[key]+=1
    
    for key in ransom:
        ransDictionary[key] +=1
    
    for each in ransom:
        if magDictionary[each] >= ransDictionary[each]:
            count +=1
    
    if count == len(ransom):
        return True 
    
    return False

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
