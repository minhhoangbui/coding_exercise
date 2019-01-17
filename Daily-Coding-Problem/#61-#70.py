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

def prob_62(a_list, target):
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
    pass
    
if __name__ == '__main__':
    print prob_61(2, 1000)