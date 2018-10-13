'''
Some applications of recursion in programming
'''
from __future__ import print_function
import copy

def permuteString(string):
    def permuteHelper(string, chosen):
        if string == []:
            tmp = ''.join(chosen)
            if tmp not in output:
                output.append(tmp)
            
            # tmp = copy.copy(chosen)
            # if tmp not in output:
            #     output.append(chosen)
        else:
            for i in range(len(string)):
                # choose
                chosen.append(string[i])
                string.pop(i)

                #explore
                permuteHelper(string, chosen)

                # un-choose
                char = chosen.pop() 
                string.insert(i, char)
                
    string = list(string)
    chosen = []
    output = []
    permuteHelper(string, chosen)
    return output

def solveNQueen(n):

    def _check(position, queen):
        for pos in position:
            if pos[0] == queen[0] or pos[1] == queen[1] or \
                sum(pos) == sum(queen) or pos[1] - pos[0] == queen[1] - queen[0]:
                return False
        return True

    def solverHelper(position, row):
        if row == n:
            print(position)
            position.pop()
        else:
            for col in range(n):
                queen = [row, col]
                if _check(position, queen):
                    position.append(queen)
                    solverHelper(position, row + 1)
            # print(position)
            if position != []:
                position.pop()
    if n < 4:
        raise ValueError('There will be no placement for that number')
    solverHelper([], 0)

def find_min_matrix_sum(mat):
    '''Given a matrix with values, find a way going from the top-left to the bottom-right with the lowest cost'''
    if len(mat) == 1 and len(mat[0]) == 1:
        return mat[0][0]
    elif len(mat) == 1:
        mat1 = [lst[1:] for lst in mat]
        return mat[0][0] + find_min_matrix_sum(mat1)
    elif len(mat[0]) == 1:
        mat2 = mat[1:]
        return mat[0][0] + find_min_matrix_sum(mat2)
    else:
        mat1 = [lst[1:] for lst in mat]
        mat2 = mat[1:]
        return mat[0][0] + min(find_min_matrix_sum(mat1),
                    find_min_matrix_sum(mat2))

def rob_house(alist):
    '''House Robber problem from LeetCode'''
    if len(alist) == 0:
        return 0
    elif len(alist) == 1:
        return alist[0]
    else:
        return max(alist[0] + rob_house(alist[2:]), rob_house(alist[1:]))

def rob_house_2(alist):
    '''House Robber II from LeetCode'''

    temp1 = rob_house(alist[:len(alist) - 1])
    temp2 = rob_house(alist[1:])
    return max(temp1, temp2)

def find_min_triangle_sum(triangle):
    '''Solve Triangle problem from LeetCode'''
    def _compute_sum(i, j):
        if j == len(triangle):
            return 0
        else:
            return triangle[j][i] + min(_compute_sum(i, j + 1), _compute_sum(i + 1, j + 1))
    return _compute_sum(0, 0)

if __name__ == '__main__':
    print(rob_house_2([1, 2, 3, 1]))




