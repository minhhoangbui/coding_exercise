'''Solve Daily Coding Problems from #71-#80'''

def prob_71():
    '''
    Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, 
    implement a function rand5() that returns an integer from 1 to 5 (inclusive).
    '''
    import random

    def _rand7():
        return random.randint(1, 7)
    
    return int(_rand7() * 5.0 / 7)

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
    print prob_77([(1, 3), (5, 8), (4, 10), (20, 25)])