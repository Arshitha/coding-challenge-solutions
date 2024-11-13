#dictionary within a dictionary inefficient
from collections import defaultdict
import itertools

_end = '_end_'
contactList = []
root = dict()
def addName(contact):
    global root
    contactList.append(contact)
    #print(contactList)
    for each in contactList:
        current_dict = root
        for letter in each:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    #print(root) 
    
def findName(root, partial):
    global contactList
    global count
    count = 0
    current_dict = root
    i=0
    for letter in partial:
        i+=1
        if letter in current_dict:
            current_dict = current_dict[letter]
            if i == len(partial):
                print(current_dict.items())
                recurDict(current_dict)   
        else:
            return 0
    return count

def recurDict(dictionary):
    global count
    for val in dictionary.values():
        if val == "_end_":
            count += 1 
        elif isinstance(val, dict):
            return recurDict(val)
    return count
    

        
