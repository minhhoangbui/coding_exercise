'''
Some algorithms which use Stack data structure
'''
from __future__ import print_function
from stack import Stack

def checkBalanceParentheses(string):
    '''
    To check whether the parentheses in the string are balanced or not
    '''
    found = False
    stack = Stack()
    assert stack.size() == 0
    for s in string:
        if s == '(':
            stack.push('x')
            found = True
        elif s == ')':
            if stack.is_empty():
                raise ValueError('The syntax of the string is a mess')
            else:
                stack.pop()
        else:
            continue
    if not found:
        print('There is no parentheses in the string')
    else:
        if stack.is_empty():
            return True
        else:
            return False

def checkBalanceSymbols(string):
    '''
    To check whether the the group [,{,(,),},] in the string are balanced or not
    '''

    def matches(opener, closer):
        open_group = '{[('
        close_group = '}])'
        return open_group.index(opener) == close_group.index(closer)

    balanced  = True
    stack = Stack()
    assert stack.size() == 0
    for s in string:
        if s in '[{(':
            stack.push(s)
        elif s in ')}]':
            if stack.is_empty():
                raise ValueError('The syntax of the string is a mess')
            else:
                top = stack.pop()
                if not matches(top, s):
                    balanced = False
        else:
            continue
    return balanced

def convertDecimalToBinary(number):
    stack = Stack()
    while number > 0:
        rem = number % 2
        stack.push(rem)
        number = number // 2
    binary = []
    while not stack.is_empty():
        binary.append(str(stack.pop()))
    return ''.join(binary)

def convertDecimal(number, base):
    digits = '0123456789ABCDEF'
    stack = Stack()
    while number > 0:
        rem = number % base
        stack.push(rem)
        number = number // base
    
    output = []
    while not stack.is_empty():
        output.append(str(digits[stack.pop()]))
    return ''.join(output)

class TowerOfHanoi(object):
    '''
    Solve the Tower of Hanoi using recursion and stack data structure
    '''
    def __init__(self):
        self.tower = [Stack(), Stack(), Stack()]

    def __call__(self, numDisks, src, dest):
        assert src < 3
        assert dest < 3
        temp = [0, 1, 2]
        temp.remove(src)
        temp.remove(dest)
        aux = temp[0]

        for i in range(numDisks, 0, -1):
            self.tower[src].push(i)
        self.moveTower(numDisks, src, aux, dest)
        
    
    def moveDisk(self, src, dest):
        return self.tower[dest].push(self.tower[src].pop())

    def moveTower(self, numDisks, src, aux, dest):
        if numDisks == 1:
            self.moveDisk(src, dest)
        else:
            self.moveTower(numDisks-1, src, dest, aux)
            self.moveDisk(src, dest)
            self.moveTower(numDisks-1, aux, src, dest)

if __name__ == '__main__':
    print(checkBalanceParentheses('((()))'))
    print(checkBalanceSymbols('[{()]'))
    print(convertDecimalToBinary(986))
    print(convertDecimal(986, 16))
    