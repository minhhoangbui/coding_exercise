'''Solve Daily Coding Problems from #71-#80'''

class Node(object):
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
        new_node = Node(value, self._head)
        self._head = new_node
        self.size += 1
    
    def remove_head(self):
        self._head = self._head.get_next()
        self.size -= 1
    
    def get_head(self):
        return self._head
    
    def set_head(self, node):
        self._head = node
    
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

def prob_71():
    '''
    Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, 
    implement a function rand5() that returns an integer from 1 to 5 (inclusive).
    '''
    import random

    def _rand7():
        return random.randint(1, 7)
    
    return int(_rand7() * 5.0 / 7)

def prob_73(linked_list):
    '''
    Given the head of a singly linked list, reverse it in-place.
    '''
    head = linked_list.get_head()
    current = head.get_next()
    head.set_next(None)
    last_node = head
    next_node = current.get_next()
    while next_node:
        current.set_next(last_node)
        last_node = current
        current = next_node
        next_node = current.get_next()
    current.set_next(last_node)
    linked_list.set_head(current)

def prob_75(a_list):
    '''
    Given an array of numbers, find the length of the longest increasing subsequence in the array. 
    The subsequence does not necessarily have to be contiguous.

    For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest 
    increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
    '''
    pass

def prob_77(a_list):
    '''
    Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping 
    intervals have been merged.

    The input list is not necessarily ordered in any way.

    For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
    '''
    pass

def prob_79(a_list):
    '''
    Given an array of integers, write a function to determine whether the array could become non-decreasing 
    by modifying at most 1 element.

    For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 
    to make the array non-decreasing.

    Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a 
    non-decreasing array.
    '''
    pass

if __name__ == '__main__':
    node = Node(10)
    linked = SinglyLinkedList(node)
    linked.insert_head(12)
    linked.insert_head(45)
    linked.insert_head(22)
    prob_73(linked)
    linked.print_list()