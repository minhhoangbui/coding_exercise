""" Implement Priority Queue class and its method in Python 2"""
import abc

class Item:
    def __init__(self, k, v):
        self.key = k
        self.value = v

class PriorityQueueBase:
    """Abstract Base Class for Priority Queue"""

    @abc.abstractmethod
    def add(self, item):
        pass
    
    @abc.abstractmethod
    def min(self):
        pass
    
    @abc.abstractmethod
    def remove_min(self):
        pass
    
    def len(self):
        return len(self)
    
    def is_empty(self):
        return len(self) == 0

class UnsortedPriorityQueue(PriorityQueueBase):
    """ A min-oriented priority queue implemented with an unsorted list"""
    

class SortedPriorityQueue(PriorityQueueBase):
    """ """
    pass

