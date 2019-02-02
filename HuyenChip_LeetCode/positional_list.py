''' An implementation of Positional List ADT'''

class _DoublyLinkedList:
    class _Node:
        def __init__(self, value=None, prev_node=None, next_node=None):
            self._value = value
            self._next = next_node
            self._prev = prev_node
    
    def __init__(self):
        self._header = self._Node()
        self._trailer = self._Node()
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return len(self) == 0
    
    def _insert_between(self, value, predecessor, successor):
        current = self._Node(value, predecessor, successor)
        predecessor._next = current
        successor._prev = current
        self._size += 1
        return current
    
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        node._prev = node._next = node._value = None

class PositionalList(_DoublyLinkedList):
    
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def value(self):
            return self._node._value
        
        def __eq__(self, other):
            return type(self) is type(other) and other._node is self._node
        
        def __ne__(self, other):
            return not (self == other)
        
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be an instance of Position')
        if p._container is not self:
            raise ValueError('p does not belong to this list')
        if p._node._next is None:
            raise ValueError('p is no longer a member of this list')
        return p._node
    
    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)
    
    def last(self):
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor._node.value()
            cursor = self.after(cursor)
            
