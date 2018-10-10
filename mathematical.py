'''Solve some mathematical problems'''

from __future__ import print_function
import copy

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

def find_year_max_population(lists):
    min_born = lists[0][0]
    max_dead = lists[0][1]
    for (born, dead) in lists:
        if born < min_born:
            min_born = born
        if dead > max_dead:
            max_dead = dead
    max_occurrence = 0
    max_year = None
    for year in range(min_born, max_dead + 1):
        occurence = 0
        for (born, dead) in lists:
            if year >= born and year <= dead:
                occurence += 1
        if occurence > max_occurrence:
            max_occurrence = occurence
            max_year = year
    return max_year

def lc_two_sum(nums, target):
    '''Solve Two Sum from leetcode in O(n)'''
    
    for idx, val in enumerate(nums):
        tmp = copy.copy(nums)
        residual = target - val
        tmp.remove(val)
        if residual in nums:
            return [idx, nums.index(residual)]

def lc_reverse_integer(num):
    if num >= 0:
        string = list(str(num))
        string.reverse()
        return int(''.join(string))
    else:
        string = list(str(abs(num)))
        string.reverse()
        return int(''.join(string)) * -1

def sieve_prime(n):
    a_list = list(range(2, n + 1))
    p = 0
    while p < len(a_list):
        i = n / a_list[p]
        for e in range(2, i + 1):
            tmp = e * a_list[p]
            if tmp in a_list:
                a_list.remove(e * a_list[p])
        p += 1
    return a_list

def count_digit_occurence(n):
    occurence_array = [0] * 10
    for i in range(0, 10):
        for j in range(n + 1):
            j = list(str(j))
            if str(i) in j:
                occurence_array[i] += 1
    return occurence_array

if __name__ == '__main__':
    print(sieve_prime(100))