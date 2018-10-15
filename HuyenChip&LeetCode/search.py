'''
An implementation of searching techniques in Python
'''
from __future__ import print_function

def sequential_search(a_list, item):
    found = False
    pos = 0
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        pos += 1
    return found

def binary_search(a_list, item):

    first = 0
    last = len(a_list)
    found = False

    while first <= last and not found:
        middle = (first + last) // 2
        if a_list[middle] == item:
            found = True
        else:
            if a_list[middle] > item:
                last = middle - 1
            else:
                first = middle + 1
    return found

def binary_search_with_recursion(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        middle = len(a_list) // 2
    if a_list[middle] == item:
        return True
    else:
        if a_list[middle] > item:
            return binary_search_with_recursion(a_list[:middle], item)
        else:
            return binary_search_with_recursion(a_list[middle + 1:], item)

if __name__ == '__main__':
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binary_search(test_list, 8))