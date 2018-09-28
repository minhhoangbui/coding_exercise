'''
An implementation of Stack data stucture

'''
from __future__ import print_function

class Stack(object):
    def __init__(self):
        self.stack = []
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return self.size() == 0
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def push(self, value):
        return self.stack.append(value)

def createStack(elements):
    stack = Stack()
    for i in elements:
        stack.push(i)
    return stack

if __name__ == '__main__':
    my_stack = createStack([8, 9, 6, 8])
    print(my_stack.size())
    print(my_stack.pop())
    