"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
from collections import defaultdict 
        
def has_cycle(head):
    addressDictionary = defaultdict(int)
    if head == None:
        return False
    else:
        currNode = head
        while currNode.next != None:
            addressDictionary[str(currNode)] +=1
            if addressDictionary[str(currNode)] > 1:
                return True
            currNode = currNode.next
        return False

    
