'''
Implementation of Krapsack problems in Python2
'''

def krapsack_with_recursion(weights, capacity, n, values):
    '''
    Solve the problems with recursive approach
    '''
    assert len(weights) == n
    assert len(values) == n
    temp = [None] * n
    temp = temp * capacity
    def _compute_value(n, cap):
        if n == 0 or cap == 0:
            return 0
        elif cap < weights[n]:
            return _compute_value(n - 1, cap)
        else:
            return max(_compute_value(n - 1, cap), values[n] + _compute_value(n - 1, cap - weights[n]))

def krabsack_with_dp(weights, capacity, n, values):
    '''
    Solve the problems with dynamic programming
    '''
    assert len(weights) == n
    assert len(values) == n


if __name__ == '__main__':
    a = ['0'] * 5
    a = [a] * 6
    print a
        