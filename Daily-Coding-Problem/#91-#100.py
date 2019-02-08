'''Solve Daily Coding Problems from #91-#100'''

def prob_96(a_list):
    '''
    Given a number in the form of a list of digits, return all possible permutations.

    For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
    '''
    def _helper(src, dst):
        if len(src) == 0:
            print(dst)
            dst.pop()
        else:
            for i in xrange(len(src)):
                dst.append(src[i])
                _helper(src[0:i] + src[i+1:], dst)
            if len(dst) != 0:
                dst.pop()
    _helper(a_list, [])


def prob_98(a_list, target):
    '''
    Given a 2D board of characters and a word, find if the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those 
    horizontally or vertically neighboring. The same letter cell may not be used more than once.

    For example, given the following board:

    [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]
    exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
    '''
    locations = []
    for i in range(len(a_list)):
        for j in range(len(a_list[0])):
            if a_list[i][j] == target[0]:
                locations.append([i, j])
    pass
    
if __name__ == '__main__':
    prob_96([1, 2, 3, 4])