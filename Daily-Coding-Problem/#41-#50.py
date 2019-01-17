'''Solve Daily Coding Problems from #41-#50'''

def prob_42(a_list, target):
    '''
    Given a list of integers S and a target number k, write a function that returns a subset of S 
    that adds up to k. If such a subset cannot be made, then return null.

    Integers can appear more than once in the list. You may assume all numbers in the list are positive.

    For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
    '''
    temp = []
    def _helper(output, target, a_list):
        if target == 0:
            print output
            output.pop()
        else:
            for i in a_list:
                if target - i >= 0:
                    output.append(i)
                    a_list.remove(i)
                    temp.append(i)
                    _helper(output, target - i, a_list)
            if output != []:
                output.pop()
                a_list.insert(0, temp.pop()) 
    output = []
    _helper(output, target, a_list)

def prob_44(a_list):
    '''
    We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] 
    and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

    Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

    You may assume each element in the array is distinct.

    For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: 
    (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
    '''
    output = []
    for start_idx in range(len(a_list) - 1):
        for query_idx in range(start_idx + 1, len(a_list)):
            if a_list[start_idx] > a_list[query_idx]:
                output.append([a_list[start_idx], a_list[query_idx]])
    return len(output)

def prob_46(string):
    '''
    Given a string, find the longest palindromic contiguous substring. If there are more than one with 
    the maximum length, return any one.

    For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic 
    substring of "bananas" is "anana".
    '''
    def _check_palindromic(string):
        str_length = len(string)
        if str_length == 1:
            return True
        elif str_length == 2:
            return string[0] == string[1]
        else:
            for i in range(str_length / 2):
                if string[i] != string[str_length - 1 - i]:
                    return False
            return True
    longest_string = ''
    for start_idx in range(0, len(string)):
        for length in range(1, len(string) - start_idx + 1):
            candidate = string[start_idx: start_idx+length]
            if _check_palindromic(candidate):
                if len(candidate) > len(longest_string):
                    longest_string = candidate
    return longest_string

def prob_47(a_list):
    '''
    Given a array of numbers representing the stock prices of a company in chronological order, write a 
    function that calculates the maximum profit you could have made from buying and selling that stock once. 
    You must buy before you can sell it.

    For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars 
    and sell it at 10 dollars.
    '''
    profit = dict().fromkeys(a_list, 0)
    for i in range(len(a_list) - 1):
        profit[a_list[i]] = max(a_list[i+1:]) - a_list[i]
    max_key = None
    max_value = 0
    for k, v in profit.iteritems():
        if v > max_value:
            max_key = k
            max_value = v
    return max_key

if __name__ == '__main__':
    print prob_44([5, 4, 3, 2, 1])