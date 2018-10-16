""" Implement Priority Queue class and its method in Python 2"""

class PriorityQueueBase:
    """Abstract Base Class for Priority Queue"""
    class _Item:
        """ Lightweight composite to store elements in priority queue"""
        __slot__ = '_key', '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __lt__(self, other):
            return self._key < other._key
    
    def is_empty(self):
        return len(self) == 0

