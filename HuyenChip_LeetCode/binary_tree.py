'''
Implementation of Tree data structure in Python 2
'''
from __future__ import print_function
from abc import abstractmethod

class Tree:

    class Position:
        
        @abstractmethod
        def element(self):
            pass
        
        @abstractmethod
        def __eq__(self, other):
            pass
        
        def __ne__(self, other):
            return not (self == other)

    @abstractmethod
    def root(self):
        pass

    def is_root(self, p):
        return self.root() == p

    @abstractmethod
    def parent(self, p):
        pass
    
    @abstractmethod
    def num_children(self, p):
        pass

    @abstractmethod
    def children(self, p):
        pass

    def is_leaf(self, p):
        return self.num_children(p) == 0
    
    @abstractmethod
    def __len__(self):
        pass

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if p == self.root():
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    
    def _height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))
    
    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height(p)

class _BinaryTree(Tree):

    @abstractmethod
    def left(self, p):
        pass

    @abstractmethod
    def right(self, p):
        pass

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.left(parent):
            return self.right(parent)
        if p == self.right(parent):
            return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    

class LinkedBinaryTree(_BinaryTree):
    
    class _Node:
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    
    class Position(_BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node
    
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be a Position')
        if p._container is not self:
            raise ValueError('This position belongs to the other Tree')
        if p._node._parent is p._node:
            raise ValueError('This node is invalid')
        return p._node
    
    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0
    
    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    
    def add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._root = self._Node(e)
        self._size = 1
        return self._make_position(self._root)

    def add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        node._left = self._Node(e, node)
        self._size += 1
        return self._make_position(node._left)

    def add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        node._right = self._Node(e, node)
        self._size += 1
        return self._make_position(node._right)

    def replace(self, p, e):
        node = self._validate(p)
        node._element = e
    
    def delete(self, p):
        if self.num_children(p) == 2:
            raise ValueError('Too many children')
        node = self._validate(p)
        child = node._left if node._left is not None else node._right
        if node._parent is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def preorder_show(self, p):
        print(p.element())
        for c in self.children(p):
            self.preorder_show(c)
    
    def postorder_show(self, p):
        for c in self.children(p):
            self.postorder_show(c)
        print(p.element())

if __name__ == '__main__':
    tree = LinkedBinaryTree()
    pos1 = tree.add_root(1)
    pos2 = tree.add_left(pos1, 2)
    pos3 = tree.add_right(pos1, 3)
    pos4 = tree.add_left(pos2, 4)
    pos5 = tree.add_right(pos2, 5)
    pos6 = tree.add_left(pos3, 6)
    tree.postorder_show(pos1)


