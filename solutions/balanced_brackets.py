class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, element):
        self.items.append(element)
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
         return len(self.items)

def is_matched(expression):
    s = Stack()
    for each in expression:
        if each == '(' or each == '{' or each == '[':
            s.push(each)
        elif (each == ')' or each == '}' or each == ']') and (s.isEmpty() == False):
            if s.peek() == '(' and each == ')':
                s.pop()
            elif s.peek() == '{' and each == '}':
                s.pop()
            elif s.peek() == '[' and each == ']':
                s.pop()
        elif (each == ')' or each == '}' or each == ']') and (s.isEmpty() == True):
            return False
        
    if s.isEmpty() == True:
        return True
    else:
        return False
                

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
