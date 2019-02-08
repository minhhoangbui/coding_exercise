''' Some common classes which helps us to complete the assignment'''
from abc import ABCMeta, abstractmethod

class Stack(object):
    def __init__(self):
        self.stack = []
    
    def __len__(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        popped = self.stack.pop()
        return popped

class Queue(object):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0
    
    def enqueue(self, element):
        self._data.append(element)
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        value = self._data[0]
        self._data = self._data[1:]
        return value

class SNode(object):
    def __init__(self, value=None, next_node=None):
        self._value = value
        self._next = next_node
    
    def get_value(self):
        return self._value
    
    def get_next(self):
        return self._next
    
    def set_next(self, node):
        self._next = node

class SinglyLinkedList(object):

    def __init__(self, node):
        self._head = node
        self.size = 1
    
    def __len__(self):
        return self.size
    
    def insert_head(self, value):
        new_node = SNode(value, self._head)
        self._head = new_node
        self.size += 1
    
    def remove_head(self):
        self._head = self._head.get_next()
        self.size -= 1
    
    def get_head(self):
        return self._head._value
    
    def remove_nth_node(self, nth):
        if nth == len(self):
            current = self._head.get_next()
            for _ in xrange(nth - 3):
                current = current.get_next()
            current.set_next(None)
            self.size -= 1
        elif nth == 1:
            self.remove_head()
        else:
            before_nth = self._head.get_next()
            for _ in xrange(nth - 3):
                before_nth = before_nth.get_next()
            nth = before_nth.get_next()
            after_nth = nth.get_next()
            before_nth.set_next(after_nth)
            self.size -= 1
    
    def print_list(self):
        current = self._head
        while current:
            print(current._value)
            current = current.get_next()

class DNode(object):
    def __init__(self, value=None, next_node=None, prev_node=None):
        self._value = value
        self._next = next_node
        self._prev = prev_node
    

class DoublyLinkedList(object):
    def __init__(self):
        self.trailer = DNode(None, None, None)
        self.header = DNode(None, None, None)
        self.trailer._prev = self.header
        self.header._next = self.trailer
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def insert_node(self, prev_node, next_node, node):
        node._prev = prev_node
        node._next = next_node
        prev_node._next = node
        next_node._prev = node
        self._size += 1
        return node
    
    def delete_node(self, node):
        next_node = node._next
        prev_node = node._prev
        next_node._prev = prev_node
        prev_node._next = next_node
        self._size -= 1
        value = node._value
        node._prev = node._next = node._value = None
        return value

    def to_list(self):
        res = []
        current_node = self.header._next
        current_value = current_node._value
        while current_value:
            res.append(current_value)
            current_node = current_node._next
            current_value = current_node._value
        return res
    
    def reverse(self):
        next_node = self.header._next
        self.header._next = None
        self.header._prev = next_node
        current_node = next_node
        while current_node._value:
            next_node = current_node._next
            last_node = current_node._prev
            current_node._next = last_node
            current_node._prev = next_node
            current_node = next_node
        next_trailer = self.trailer._prev
        self.trailer._next = next_trailer
        self.trailer._prev = None
        self.header, self.trailer = self.trailer, self.header

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
    
    def preorder_show(self, p, result=[]):
        result.append(p.element())
        for c in self.children(p):
            self.preorder_show(c)
        return result

    def postorder_show(self, p, result=[]):
        def _helper(pr):
            for c in self.children(pr):
                self.postorder_show(c)
            result.append(pr.element())
        _helper(p)
        return result

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
    
    def inorder_show(self, p, result=[]):
        lc = self.left(p)
        if lc is not None:
            self.inorder_show(lc)
        result.append(p.element())
        rc = self.right(p)
        if rc is not None:
            self.inorder_show(rc)
        return result
    
    def breadthfirst_show(self):
        queue = Queue()
        result = []
        queue.enqueue(self.root())
        while not queue.is_empty():
            p = queue.dequeue()
            result.append(p.element())
            for c in self.children(p):
                queue.enqueue(c)
        return result
    
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(3)
    queue.dequeue()
    print queue.is_empty()
    queue.dequeue()
    print queue.is_empty()
