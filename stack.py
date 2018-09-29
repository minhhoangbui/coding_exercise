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
    
    def peek(self):
        return self.stack[-1]

def createStack(elements):
    stack = Stack()
    for i in elements:
        stack.push(i)
    return stack

if __name__ == '__main__':
    my_stack = Stack()
    print(my_stack.is_empty())
    my_stack.push(4)
    my_stack.push('dog')
    print(my_stack.peek())
    my_stack.push(True)
    print(my_stack.size())
    print(my_stack.is_empty())
    my_stack.push(8.4)
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.size())
    