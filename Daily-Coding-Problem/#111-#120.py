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

if __name__ == '__main__':
    tree = LinkedBinaryTree()
    pos1 = tree.add_root(100)
    pos2 = tree.add_left(pos1, 7)
    pos3 = tree.add_right(pos1, 6)
    pos4 = tree.add_left(pos2, 1)
    pos5 = tree.add_right(pos2, 2)
    pos6 = tree.add_left(pos3, 8)
    pos7 = tree.add_right(pos3, 4)
    print(prob_117(tree))
