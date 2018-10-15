'Solve Daily Coding Problems from #1-#10'
import copy
from operator import mul

def prob_1(nums, target):
    '''
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    Bonus: Can you do this in one pass?
    '''
    
    for idx, val in enumerate(nums):
        tmp = copy.copy(nums)
        residual = target - val
        tmp.remove(val)
        if residual in nums:
            return True
        return False

def prob_2(a_list):
    '''
    Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
    '''
    output = []
    for i in range(len(a_list)):
        temp = copy.copy(a_list)
        temp.pop(i)
        output.append(reduce(mul, temp))
    return output

if __name__ == '__main__':
    nums = [3, 2, 1]

    print prob_2(nums)
