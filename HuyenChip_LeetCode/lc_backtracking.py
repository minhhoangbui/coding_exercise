""" Some problems of Back Tracking from LeetCode"""

import copy
from sort import selection_sort

def subset(a_list):
    pass

def combination_sum(a_list, target):
    chosen = []
    output = []

    def _check_duplicate(chosen, output):
        if len(output) == 0:
            return False
        selection_sort(chosen)
        for e in output:
            selection_sort(e)
            if chosen == e:
                return True
        return False

    def _helper(a_list, target):
        if target == 0:
            temp = list(chosen)
            if not _check_duplicate(temp, output):
                output.append(temp)
        elif target < min(a_list):
            pass
        else:
            for i in a_list:
                chosen.append(i)
                _helper(a_list, target - i)
                chosen.pop()
    _helper(a_list, target)
    print output

def combination_sum_2(a_list, target):
    chosen = []
    output = []

    def _check_duplicate(chosen, output):
        if len(output) == 0:
            return False
        selection_sort(chosen)
        for e in output:
            selection_sort(e)
            if chosen == e:
                return True
        return False

    def _helper(a_list, target):
        if target == 0:
            temp = list(chosen)
            if not _check_duplicate(temp, output):
                output.append(temp)
        elif len(a_list) == 0:
            pass
        elif target < min(a_list):
            pass
        else:
            for i in range(len(a_list)):
                temp_list = list(a_list[i:])
                temp_num = temp_list.pop(0)
                chosen.append(temp_num)
                _helper(temp_list, target - temp_num)
                chosen.pop()
    _helper(a_list, target)
    print output

if __name__ == '__main__':
    combination_sum_2([2,5,2,1,2], 5)
