'''Solve sorted list merging from LeetCode'''
from __future__ import print_function

def two_sorted_sort(list_a, list_b):
    i = 0
    j = 0
    sorted_list = []
    while i < len(list_a) and j < len(list_b):
        if list_a[i] <  list_b[j]:
            sorted_list.append(list_a[i])
            i += 1
        else:
            sorted_list.append(list_b[j])
            j += 1
    
    while i < len(list_a):
        sorted_list.append(list_a[i])
        i += 1
    
    while j < len(list_b):
        sorted_list.append(list_b[j])
        j += 1
    return sorted_list

def k_sorted_sort(list_of_lists):
    sorted_list = list_of_lists[0]
    for a_list in list_of_lists[1:]:
        sorted_list = two_sorted_sort(sorted_list, a_list)
    return sorted_list

def remove_duplicate_sorted_list(a_list):
    b_list = []
    for i in a_list:
        if i not in b_list:
            b_list.append(i)
    return b_list

if __name__ == '__main__':
    a_list = k_sorted_sort([[1, 4, 5], [1, 3, 4], [2, 6]])
    print(remove_duplicate_sorted_list(a_list))
    