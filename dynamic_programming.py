'''
Some examples of dynamic programming in python 2
'''
from __future__ import print_function

def fibonacci_sequence_with_loop(nth):
    assert nth >= 0
    fibo_seq = [0, 1]
    if nth < 2:
        return fibo_seq[nth]
    else:
        while len(fibo_seq) < nth + 1:
            fibo_seq.append(fibo_seq[-1] + fibo_seq[-2])
        return fibo_seq[nth]

def fibonacci_sequence_with_recursion(nth_element):
    assert nth_element >= 0
    if nth_element == 0:
        return 0
    if nth_element == 1:
        return 1
    else:
        return fibonacci_sequence_with_recursion(nth_element - 2) + fibonacci_sequence_with_recursion(nth_element - 1)

def fibonacci_sequence_with_memoization(nth):
    memo = [None] * (nth + 1)
    def fibo(nth):
        if memo[nth] is not None:
            return memo[nth]
        else:
            if nth == 0:
                result = 0
            elif nth == 1:
                result = 1
            else:
                result = fibo(nth - 2) + fibo(nth - 1)
            memo[nth] = result
        return result
    return fibo(nth)
    
    
def find_longest_subsequence_with_recursion(first_string, second_string):
    '''
    Find the longest subsequence between two strings
    For exp:
    1st string = 'abcdad'
    2nd string = 'acbcf'
    >>> 'abcf'
    '''
    if not first_string or not second_string:
        return ''
    x, xs, y, ys = first_string[0], first_string[1:], second_string[0], second_string[1:]
    if x == y:
        return x + find_longest_subsequence_with_recursion(xs, ys)
    return max(find_longest_subsequence_with_recursion(xs, second_string),
            find_longest_subsequence_with_recursion(ys, first_string), key=len)


if __name__ == '__main__':
    print(fibonacci_sequence_with_memoization(9))
