# -*- coding: utf-8 -*-
'''Solve Daily Coding Problems from #31-#40'''
from outils import LinkedBinaryTree

def prob_31(string1, string2):
    '''
    The edit distance between two strings refers to the minimum number of character insertions, 
    deletions, and substitutions required to change one string to the other. For example, the edit 
    distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” 
    for “i”, and append a “g”.

    Given two strings, compute the edit distance between them.
    '''
    if len(string1) > len(string2):
        string1, string2 = string2, string1
    
    distances = range(len(string2) + 1)
    for i2, c2 in enumerate(string2):
        distances_ = [i2 + 1]
        for i1, c1 in enumerate(string1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min(distances[i1], distances[i1 + 1], distances_[-1]))
        distances = distances_
    return distances[-1]

def prob_33(a_list):
    '''
    Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out 
    the median of the list so far on each new element.

    Recall that the median of an even-numbered list is the average of the two middle numbers.

    For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

    2
    1.5
    2
    3.5
    2
    2
    2
    '''

    def _print_median(a_list):
        if len(a_list) % 2 == 1:
            print a_list[len(a_list) / 2]
        else:
            print (a_list[len(a_list) / 2] + a_list[len(a_list) / 2 - 1]) / 2.0
    
    import bisect
    stream_list = []
    for i in a_list:
        bisect.insort_left(stream_list, i)
        _print_median(stream_list)

def prob_35(a_list):
    '''
    Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that 
    all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

    Do this in linear time and in-place.

    For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
    '''
    a_dict = {'R': 1, 'G': 2, 'B': 3}
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_dict[a_list[i]] > a_dict[a_list[i + 1]]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
    return a_list

def prob_36(tree, root):
    '''
    Given the root to a binary search tree, find the second largest node in the tree.
    '''
    a_list = tree.preorder_show(root)
    a_list = sorted(a_list)
    return a_list[-2]

def prob_37(a_list):
    '''
    The power set of a set is the set of all its subsets. Write a function that, given a set, 
    generates its power set.

    For example, given the set {1, 2, 3}, it should return 
    {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
    '''
    
    def _helper(subset, a_list, idx):
        if idx == len(a_list):
            output = [e for e in subset if e is not None]
            print output
        else:
            subset[idx] = None
            _helper(subset, a_list, idx + 1)
            subset[idx] = a_list[idx]
            _helper(subset, a_list, idx + 1)
    
    subset = [None, ] * len(a_list)
    _helper(subset, a_list, 0)
    
def prob_38(N):
    '''
    You have an N by N board. Write a function that, given N, returns the number of possible arrangements of 
    the board where N queens can be placed on the board without threatening each other, i.e. no two queens share 
    the same row, column, or diagonal.
    '''
    def _check_validity(position, queen):
        for p in position:
            if p[0] == queen[0] or p[1] == queen[1] or \
                sum(p) == sum(queen) or p[1] - p[0] == queen[0] - queen[1]:
                return False
        return True
        
    
    def _solve_helper(position, row):
        if row == N:
            print(position)
            position.pop()
        else:
            for col in range(N):
                queen = [row, col]
                if _check_validity(position, queen):
                    position.append(queen)
                    _solve_helper(position, row + 1)
            if position != []:
                position.pop()
    if N < 4:
        raise ValueError("It's not possible to find the solution")
    _solve_helper([], 0)

def prob_40(a_list):
    '''
    Given an array of integers where every integer occurs three times except for one integer, which 
    only occurs once, find and return the non-duplicated integer.

    For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

    Do this in O(N) time and O(1) space.
    '''
    output = []
    for i in a_list:
        if i not in output:
            output.append(i)
        else:
            output.remove(i)
    return output[0]

if __name__ == '__main__':
    tree = LinkedBinaryTree()
    pos1 = tree.add_root(1)
    pos2 = tree.add_left(pos1, 2)
    pos3 = tree.add_right(pos1, 3)
    pos4 = tree.add_left(pos2, 4)
    pos5 = tree.add_right(pos2, 5)
    pos6 = tree.add_left(pos3, 6)
    print tree.postorder_show(pos1)
    # print prob_36(tree, pos1)