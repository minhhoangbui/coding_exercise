'''Solve Daily Coding Problems from #111-#120'''

from outils import LinkedBinaryTree

def prob_113(string):
    '''
    Given a string of words delimited by spaces, reverse the words in string. For example, 
    given "hello world here", return "here world hello"

    Follow-up: given a mutable string representation, can you perform this operation in-place?
    '''
    string = string.split(' ')
    string_len = len(string)
    for i in range(string_len // 2):
        temp = string[i]
        string[i] = string[string_len - 1 - i]
        string[string_len - 1 - i] = temp
    return ' '.join(string)

def prob_114(string, pattern):
    '''
    Given a string and a set of delimiters, reverse the words in the string while maintaining the 
    relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"

    Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
    '''
    import re
    delims = pattern.split('|')
    delim_list = [s for s in string if s in delims]
    string = re.split(pattern, string)
    string = [s for s in string if s != '']
    if len(delim_list) != len(string):
        delim_list.append('')
    string = reversed(string)
    result = ''
    for s, d in zip(string, delim_list):
        result += s
        result += d
    return result

def prob_117(tree):
    '''
    This problem was asked by Facebook.

    Given a binary tree, return the level of the tree with minimum sum.
    '''

    nodes = tree.breadthfirst_show()
    
    import math
    depth = math.log(len(nodes) + 1) - 1
    if depth != int(depth):
        depth = int(depth) + 1
    else:
        depth = int(depth)
    level_sum = [None] * (depth + 1)
    curr = 0
    for d in xrange(depth + 1):
        level_sum[d] = sum(nodes[curr: curr + 2**d])
        curr += 2**d        
    return level_sum.index(min(level_sum))

def prob_119(a_list):
    '''
    Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If 
    there are multiple smallest sets, return any of them.

    For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all 
    these intervals is {3, 6}.
    '''
    min_max = a_list[0][1]
    max_min = a_list[0][0]
    for e in a_list[1:]:
        if e[1] < min_max:
            min_max = e[1]
        if e[0] > max_min:
            max_min = e[0]
    return [min_max, max_min]
        

if __name__ == '__main__':
    print prob_119([[0, 3], [2, 6], [3, 4], [6, 9]])
