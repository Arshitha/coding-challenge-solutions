""" Node is defined as"""
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

tree = []

def checkBST(root):
    if root != None:
        checkBST(root.left)
        tree.append(root.data)
        checkBST(root.right)
    #print(tree)
    
    for i in range(1,len(tree)):
        if tree[i] <= tree[i-1]:
            return False
    return True
    
    
