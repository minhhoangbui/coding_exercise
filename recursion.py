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
            
if __name__ == '__main__':
    solveNQueen(5)




