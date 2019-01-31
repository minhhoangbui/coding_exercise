# -*- coding: utf-8 -*-
'''Solve Daily Coding Problems from #101-#110'''

class Node(object):
    def __init__(self, value=None, next_node=None, prev_node=None):
        self._value = value
        self._next = next_node
        self._prev = prev_node
    

class DoublyLinkedList(object):
    def __init__(self):
        self.trailer = Node(None, None, None)
        self.header = Node(None, None, None)
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

        
def prob_102(a_list, K):
    '''
    Given a list of integers and a number K, return which contiguous elements of the list sum to K.

    For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].
    '''
    pass


def prob_103(string, char_set):
    '''
    Given a string and a set of characters, return the shortest substring containing all the characters in the set.

    For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

    If there is no substring containing all the characters in the set, return null.
    '''
    pass

def prob_104(linked_list):
    '''
    Determine whether a doubly linked list is a palindrome. What if it’s singly linked?
    For example, 1 -> 4 -> 3 -> 4 -> 1 returns true while 1 -> 4 returns false.
    '''
    before = linked_list.to_list()
    linked_list.reverse()
    after = linked_list.to_list()
    return before == after

def prob_106(a_list):
    '''
    Given an integer list where each number represents the number of hops you can make, determine whether 
    you can reach to the last index starting at index 0.

    For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false.
    '''
    pass
    

if __name__ == '__main__':
    linked = DoublyLinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(2)
    node4 = Node(1)
    linked.insert_node(linked.header, linked.trailer, node1)
    linked.insert_node(linked.header, node1, node2)
    linked.insert_node(linked.header, node2, node3)
    linked.insert_node(linked.header, node3, node4)
    print prob_104(linked)