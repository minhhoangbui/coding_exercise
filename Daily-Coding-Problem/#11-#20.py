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

if __name__ == '__main__':
    print(prob_11('de', ['dog', 'deer', 'deal']))