'''Solve Daily Coding Problems from #1-#10'''
import copy
from operator import mul

def prob_1(nums, target):
    '''
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    Bonus: Can you do this in one pass?
    '''
    
    for idx, val in enumerate(nums):
        tmp = copy.copy(nums)
        residual = target - val
        tmp.remove(val)
        if residual in nums:
            return True
        return False

def prob_2(a_list):
    '''
    Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
    '''
    output = []
    for i in range(len(a_list)):
        temp = copy.copy(a_list)
        temp.pop(i)
        output.append(reduce(mul, temp))
    return output

def prob_3():
    '''
    Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes 
    the string back into the tree.

    For example, given the following Node class

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    The following test should pass:

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    '''

    class Node:
        def __init__(self, val, left=None, right=None):
            self.root = val
            self.left = left
            self.right = right
        
        def get_children(self):
            return [self.left, self.right]

    def serialize(node):
        array = []
        def encode(node):
            array.append(node.root)
            if node.get_children() != [None, None]:
                for child in node.get_children():
                    if child is not None:
                        encode(child)
                    else:
                        array.append('#')
        encode(node)
        return ' '.join(array)

    def deserialize(string):
        def decode(array):
            if array:
                val = array.pop(0)
                if val == '#':
                    return None
                node = Node(val)
                node.left = decode(array)
                node.right = decode(array)
                return node
        
        array = string.split(' ')
        return decode(array)
    
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    string = serialize(node)
    assert deserialize(string).left.left.root == 'left.left'

def prob_4(a_list):
    """
    Given an array of integers, find the first missing positive integer in linear time and constant space. 
    In other words, find the lowest positive integer that does not exist in the array. The array can contain 
    duplicates and negative numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

    You can modify the input array in-place.
    """
    i = 1
    while i > 0:
        if i not in a_list:
            return i
        i += 1

def prob_5():
    """
    cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
    For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

    Given this implementation of cons:

    def cons(a, b):
        def pair(f):
            return f(a, b)
        return pair
    Implement car and cdr.
    """
    def cons(a, b):
        return [a, b]
    
    def car(cons):
        return cons[0]
    
    def cdr(cons):
        return cons[-1]
    
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4

def prob_7(message):
    '''
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

    For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

    You can assume that the messages are decodable. For example, '001' is not allowed.
    '''
    letter_dict = {k + 1: chr(k + 97) for k in range(26)} 

    def _helper(a_list, chosen):
        if not a_list:
            out = list(chosen)
            out = [''. join(i) for i in out]
            out = [letter_dict[int(i)] for i in out]
            print(''.join(out))
        else:
            temp1 = a_list[0]
            temp_lst1 = list(a_list[1:])
            chosen.append(temp1)
            _helper(temp_lst1, chosen)
            chosen.pop()
            if len(a_list) >= 2:
                temp2 = a_list[0: 2]
                if int(''.join(temp2)) <= 26:
                    temp_lst2 = list(a_list[2:])
                    chosen.append(temp2)
                    _helper(temp_lst2, chosen)
                    chosen.pop()
    
    a_list = list(message)
    chosen = []
       
    _helper(a_list, chosen)

def prob_8():
    '''
    A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

    Given the root to a binary tree, count the number of unival subtrees.

    For example, the following tree has 5 unival subtrees:

         0
        / \
       1   0
          / \
         1   0
        / \
       1   1
    '''

def prob_9(a_list):
    '''
    Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

    For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

    Follow-up: Can you do this in O(N) time and constant space?
    '''
    if not a_list:
        return 0
    temp1 = a_list[0] + prob_9(a_list[2:])
    temp2 = prob_9(a_list[1:])
    return max(temp1, temp2)

def prob_10(n):
    '''
    Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
    '''
    def _print():
        print('mhoangbui')

    start = 0
    import time

    while True:
        while time.time() - start < n:
            pass
        _print()
        start = time.time()

            
if __name__ == '__main__':
    prob_10(2)

