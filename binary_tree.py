'''
Implementation of Tree data structure in Python 2
'''
from __future__ import print_function


class BinaryTree(object):
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None
    
    def insert_left(self, node):
        if self.left is None:
            self.left = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left = self.left
            self.left = t
    
    def insert_right(self, node):
        if self.right is None:
            self.right = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right = self.right
            self.right = t
    
    def get_right(self):
        return self.right
    
    def get_left(self):
        return self.left
    
    def set_root_val(self, root_value):
        self.key = root_value
    
    def get_root_val(self):
        return self.key

if __name__ == '__main__':
    tree = BinaryTree('a')
    tree.insert_left('b')
    tree.left.insert_right('d')
    tree.insert_right('c')
    tree.right.insert_left('e')
    tree.right.insert_right('f')

