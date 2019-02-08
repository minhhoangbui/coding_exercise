'''Solve Daily Coding Problems from #61-#70'''

def prob_61(x, y):
    '''
    Implement integer exponentiation. That is, implement the pow(x, y) function, 
    where x and y are integers and returns x^y.

    Do this faster than the naive method of repeated multiplication.

    For example, pow(2, 10) should return 1024.
    '''
    import math
    return math.exp(y * math.log(x))

def prob_62(m, n):
    '''
    There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

    For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

    Right, then down
    Down, then right
    Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
    '''
    N = [[1] * n] * m
    for i in range(m - 1):
        for j in range(n - 1):
            N[i + 1][j + 1] = N[i][j + 1] + N[i + 1][j]
    return N[m - 1][n - 1]

def prob_63(a_list, target):
    '''
    Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found 
    in the matrix by going left-to-right, or up-to-down.

    For example, given the following matrix:

    [['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
    and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target 
    word 'MASS', you should return true, since it's the last row.
    '''
    target = list(target)
    found = False
    for i in range(len(a_list)):
        for j in range(len(a_list[0])):
            if a_list[i][j] == target[0]:
                try:
                    option_1 = [a_list[i][k] for k in range(j, j + len(target))]
                    res_1 = option_1 == target
                except IndexError:
                    res_1 = False
                try:
                    option_2 = [a_list[k][j] for k in range(i, i + len(target))]
                    res_2 = option_2 == target
                except IndexError:
                    res_2 = False
                if res_1 or res_2:
                    found = True
                    break
    return found

def prob_65(a_list):
    '''
    Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

    For example, given the following matrix:

    [[1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]]
    You should print out the following:

    1
    2
    3
    4
    5
    10
    15
    20
    19
    18
    17
    16
    11
    6
    7
    8
    9
    14
    13
    12
    '''
    pass

def prob_69(a_list):
    '''
    Given a list of integers, return the largest product that can be made by multiplying any three integers.

    For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

    You can assume the list has at least three integers.
    '''
    from operator import mul
    def _helper(subset, a_list, idx):
        if len(subset) == 3:
            output.append(reduce(mul, subset, 1))
            subset.pop()
        else:
            for i in a_list[idx:]:
                subset.append(i)
                _helper(subset, a_list, idx + 1)
                idx += 1
            if subset != []:
                subset.pop()
    subset = []
    output = []
    _helper(subset, a_list, 0)
    return max(output)

    
def prob_70(n):
    '''
    A number is considered perfect if its digits sum up to exactly 10.

    Given a positive integer n, return the n-th perfect number.

    For example, given 1, you should return 19. Given 2, you should return 28.
    '''
    n_ = str(10 - n)
    return int(str(n) + n_)

if __name__ == '__main__':

    print prob_62(3, 5)