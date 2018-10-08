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
    

if __name__ == '__main__':
    print(permuteString('aab'))




