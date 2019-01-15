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
    print prob_47([9, 11, 8, 5, 7, 10])