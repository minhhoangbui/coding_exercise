# -*- coding: utf-8 -*-
'''Solve Daily Coding Problems from #101-#110'''

from outils import DoublyLinkedList, LinkedBinaryTree
        
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

def prob_107(tree):
    '''
    Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

      1
     / \
    2   3
       / \
      4   5
    '''
    return tree.breadthfirst_show()

def prob_108(stringA, stringB):
    '''
    Given two strings A and B, return whether or not A can be shifted some number of times to get B.

    For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
    '''
    if len(stringA) != len(stringB):
        return False
    string_len = len(stringA)
    for i in xrange(-string_len, -1, 1):
        temp = [stringA[j] for j in xrange(i, i + string_len)]
        if ''.join(temp) == stringB:
            return True
    return False

def prob_109(bit):
    '''
    Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, 
    the 3rd and 4th bit should be swapped, and so on.

    For example, 10101010 should be 01010101. 11100010 should be 11010001.
    Bonus: Can you do this in one line?
    '''
    return ''.join([bit[i + 1] if i % 2 == 0 else bit[i - 1] for i in range(len(bit))])

def prob_110(tree):
    '''
    Given a binary tree, return all paths from the root to leaves.

    For example, given the tree

        1
       / \
      2   3
         / \
        4   5
    it should return [[1, 2], [1, 3, 4], [1, 3, 5]].
    '''
    result = []
    def _helper(tree, current):
        if tree.is_leaf(current):
            result.append(current.element())
            print(result)
            result.pop()
        else:
            result.append(current.element())
            for c in tree.children(current):
                _helper(tree, c)
            result.pop()

    root = tree.root()
    _helper(tree, root)

if __name__ == '__main__':
    tree = LinkedBinaryTree()
    pos1 = tree.add_root(1)
    pos2 = tree.add_left(pos1, 2)
    pos3 = tree.add_right(pos1, 3)
    pos4 = tree.add_left(pos3, 4)
    pos5 = tree.add_right(pos3, 5)
    prob_110(tree)