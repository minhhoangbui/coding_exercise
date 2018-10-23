'Solve Daily Coding Problems from #1-#10'
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

if __name__ == '__main__':
    print prob_9([5, 1, 1, 5])

