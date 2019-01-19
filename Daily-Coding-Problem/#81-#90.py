# -*- coding: utf-8 -*-
'''Solve Daily Coding Problems from #71-#80'''

def prob_81(a_dict, string):
    '''
    Given a mapping of digits to letters (as in a phone number), and a digit string, return 
    all possible letters the number could represent. You can assume each valid number in the 
    mapping is a single digit.

    For example if {"2": ["a", "b", "c"], "3": ["d", "e", "f"], …} then "23" should return 
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    '''
    def _helper(a_list, decoded):
        if len(decoded) == len(a_list):
            output.append(''.join(decoded))
            decoded.pop()
        else:
            for c in a_list[len(decoded)]:
                decoded += c
                _helper(a_list, decoded)
            if decoded != []:
                decoded.pop()
    
    output = []
    string = list(string)
    a_list = [a_dict[s] for s in string]
    _helper(a_list, [])
    return output

if __name__ == '__main__':
    print prob_81({"2": ["a", "b", "c"], "3": ["d", "e", "f"], "1": ["g", "h", "k"]}, '132')