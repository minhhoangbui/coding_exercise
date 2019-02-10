'''Solve Daily Coding Problems from #71-#80'''
from outils import SNode, SinglyLinkedList, Queue, LinkedBinaryTree

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
    def _check_overlap(current, e):
        if current[1] < e[0] or e[1] < current[0]:
            return False
        return True
    
    def _merge(current, e):
        return (min(current[0], e[0]), max(current[1], e[1]))

    for i in xrange(len(a_list) - 1):
        if i == len(a_list) - 1:
            break
        current = a_list[i]
        for e in a_list[i+1:]:
            if _check_overlap(current, e):
                current = _merge(current, e)
                a_list[i] = current
                a_list.remove(e)
    return a_list

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

def prob_80(tree):
    '''
    This problem was asked by Google.

    Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

        a
       / \
      b   c
     /
    d
    '''
    temp = []
    queue = Queue()
    queue.enqueue(tree.root())
    while not queue.is_empty():
        p = queue.dequeue()
        temp.append(p.element())
        for c in tree.children(p):
            queue.enqueue(c)
    return temp[-1]


if __name__ == '__main__':
    print prob_77([(1, 3), (5, 8), (4, 10), (20, 25), (-1, 2), (6, 8)])