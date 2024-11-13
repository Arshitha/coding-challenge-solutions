""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None"""

import sys
minL = -sys.maxsize - 1
maxR = sys.maxsize

def checkBST(root):
    global minL
    global maxR
    return isBST(root,minL,maxR)
    
def isBST(root, l,r):
    
    if root ==None:
        return True
    
    if root.data <= l or root.data >=r:
        return False
    
    if root.data <= l or root.data >=r:
        return False

    return isBST(root.left, l, root.data) and isBST(root.right, root.data, r)
    
    
