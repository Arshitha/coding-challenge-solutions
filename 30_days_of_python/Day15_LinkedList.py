class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next

    def insert(self, head, data):
        # Initially when the linked list is empty
        if not head:
            return Node(data)
        # Traverses through existing nodes and adds it to the tail
        else:
            currNode = head
            while currNode.next is not None:
                currNode = currNode.next
            currNode.next = Node(data)

        return head


# Input Handling
mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
