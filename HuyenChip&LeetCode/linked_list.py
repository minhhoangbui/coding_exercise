'''
    An implementation of Linked List data structure in Python.
    Each node contains a value and reference to the next node
'''
from __future__ import print_function

class Node(object):
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next_node):
        self.next_node = new_next_node

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    
    def size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.get_next()
        return size
    
    def search(self, value):
        current = self.head
        target = None
        while current:
            if current.get_value() == value:
                target = current
                break
            else:
                current = current.get_next()
        return target
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.get_next()

    def delete(self, value):
        current = self.head
        found = False
        last = None
        while current and not found:
            if current.get_value() == value:
                found = True
            else:
                last = current
                current = current.get_next()
        if not found:
            raise ValueError('Data %s is not in the list' %value)
        if last is None:
            self.head = current.get_next()
        else:
            last.set_next(current.get_next())

def creatList(elements):
    my_list = LinkedList()
    for i in elements:
        my_list.insert(i)
    return my_list

if __name__ == '__main__':
    my_list = creatList([1, 2, 3, 4, 5])
    my_list.print_list()



