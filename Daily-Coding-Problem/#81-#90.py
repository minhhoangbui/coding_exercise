# -*- coding: utf-8 -*-
'''Solve Daily Coding Problems from #71-#80'''
from outils import LinkedBinaryTree

def prob_81(a_dict, string):
    '''
    Given a mapping of digits to letters (as in a phone number), and a digit string, return 
    all possible letters the number could represent. You can assume each valid number in the 
    mapping is a single digit.

    For example if {"2": ["a", "b", "c"], "3": ["d", "e", "f"], …} then "23" should return 
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    '''
    def _helper(a_list, decoded):
        if len(decoded) == len(a_list):
            output.append(''.join(decoded))
            decoded.pop()
        else:
            for c in a_list[len(decoded)]:
                decoded += c
                _helper(a_list, decoded)
            if decoded != []:
                decoded.pop()
    
    output = []
    string = list(string)
    a_list = [a_dict[s] for s in string]
    _helper(a_list, [])
    return output

def prob_89(tree):
    '''
    Determine whether a tree is a valid binary search tree.

    A binary search tree is a tree with two children, left and right, and satisfies the constraint 
    that the key in the left child must be less than or equal to the root and the key in the right 
    child must be greater than or equal to the root.
    '''
    
    def _helper(tree, current):
        # NOTE: we could use 'nonlocal' to change the scope in nested function in Python3
        left = tree.left(current)
        right = tree.right(current)
        if left is not None:
            if left.element() > current.element():
                result['res'] = False
            _helper(tree, left)
        if right is not None:
            if right.element() < current.element():
                result['res'] = False
            _helper(tree, right)

    result = {'res': True}
    root = tree.root()
    _helper(tree, root)
    if result['res'] == False:
        return False
    return True

if __name__ == '__main__':
    tree = LinkedBinaryTree()
    pos1 = tree.add_root(9)
    pos2 = tree.add_left(pos1, 6)
    pos3 = tree.add_right(pos1, 15)
    pos4 = tree.add_left(pos2, 2)
    pos5 = tree.add_right(pos2, 7)
    pos6 = tree.add_left(pos3, 13)
    pos7 = tree.add_right(pos3, 20)
    print prob_89(tree)

