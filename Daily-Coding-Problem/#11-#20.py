# -*- coding: utf-8 -*-
'''Solve Daily Coding Problems from #11-#20'''

def prob_11(prefix, word_list):
    '''
    Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all s
    trings in the set that have s as a prefix.

    For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
    '''

    import re
    regex = prefix + '\w+'
    regex = re.compile(regex, flags=re.UNICODE)
    result = [string for string in word_list if bool(regex.search(string))]
    return result

def prob_12(N, choices):
    '''
    There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function 
    that returns the number of unique ways you can climb the staircase. The order of the steps matters.

    For example, if N is 4, then there are 5 unique ways:

        1, 1, 1, 1
        2, 1, 1
        1, 2, 1
        1, 1, 2
        2, 2
    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? 
    For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
    '''
    def _helper(rest, steps):
        if rest == 0:
            print steps
        elif rest < min(choices):
            pass
        else:
            for i in choices:
                steps.append(i)
                _helper(rest - i, steps)
                steps.pop()
    
    steps = []

    _helper(N, steps)


def prob_13(string, k0):
    '''
    Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

    For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
    '''

    output = []
    string = list(string)
    for i in range(len(string)):
        tmps = list(string[i:])
        j = k = 0
        chosen = []
        while j < len(tmps):
            if tmps[j] not in chosen:
                k += 1
            if k > k0:
                break
            chosen.append(tmps[j])
            j += 1
        output.append(chosen)
    max_string = output[0]
    max_len = len(output[0])
    for o in output[1:]:
        if len(o) > max_len:
            max_len = len(o)
            max_string = o
    return ''.join(max_string)

def prob_14():
    '''
    The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

    Hint: The basic equation of a circle is x2 + y2 = r2.
    '''
    import numpy as np 
    import math
    n_bins = 1000
    R = 7
    x = np.linspace(0, R, n_bins + 1)
    y = [math.sqrt(R * R - e * e) for e in x]
    dx = R / float(n_bins)
    S = 4 * sum(y) * dx
    return S / (R*R)

def prob_16():
    '''
    You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure 
    to accomplish this, with the following API:

        record(order_id): adds the order_id to the log
        get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

    You should be as efficient with time and space as possible.
    '''

    class Queue:
        def __init__(self, N):
            self._limit = N
            self._size = 0
            self.data = []
        
        def record(self, order_id):
            if self._size < self._limit:
                self.data.append(order_id)
                self._size += 1
            else:
                self.data = self.data[:-1]
                self.data.append(order_id)

        def get_last(self, i):
            return self.data[i]

def prob_18(a_list, k):
    '''
    Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum 
    values of each subarray of length k.

    For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)
    Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need 
    to store the results. You can simply print them out as you compute them.
    '''
    pass

def prob_19(cost_matrix):
    #TODO: check its validity
    '''
    A builder is looking to build a row of N houses that can be of K different colors. He has a goal of 
    minimizing cost while ensuring that no two neighboring houses are of the same color.

    Given an N by K matrix where the nth row and kth column represents the cost to build the nth house 
    with kth color, return the minimum cost which achieves this goal.
    '''

    def _helper(cost_matrix, current_color, current_house):
        if current_house == len(cost_matrix):
            possible_choices = [cost_matrix[current_house][i] for i in range(len(cost_matrix[0])) if i != current_color]
            return min(possible_choices)
        else:
            possible_colors = [i for i in range(len(cost_matrix[0])) if i != current_color]
            possible_outcomes = []
            for c in possible_colors:
                possible_outcomes.append(cost_matrix[current_house][c] + _helper(cost_matrix, c, current_house + 1))
                return min(possible_outcomes)
    
    return _helper(cost_matrix, None, 1)



if __name__ == '__main__':
    print prob_14()