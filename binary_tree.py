'''
Implementation of Tree data structure in Python 2
'''
from __future__ import print_function

class BinaryTree(object):
    def __init__(self, root):
        self.tree = [root, [], []]
    
    def insert_left(self, sub_branch):
        pass