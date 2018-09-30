'''
Implementation of sorting techniques in Python 2
'''
from __future__ import print_function

def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp

def improved_bubble_sort(a_list):
    '''
    Apply early stopping to bubble sort
    '''
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = a_list[i]
        pass_num -= 1

def selection_sort(a_list):
    for slot in range(len(a_list) - 1, 0, -1):
        max_pos = 0
        for loc in range(1, slot + 1):
            if a_list[loc] > a_list[max_pos]:
                max_pos = loc
        temp = a_list[slot]
        a_list[slot] = a_list[max_pos]
        a_list[max_pos] = temp

def insertion_sort(a_list):
    for idx in range(1, len(a_list)):
        current_value = a_list[idx]
        position = idx
        
        while position > 0 and current_value < a_list[position - 1]:
            a_list[position] = a_list[position - 1]
            position -= 1
        a_list[position] = current_value
            
def shell_sort(a_list):
    def gap_insertion_sort(a_list, start, gap):
        for idx in range(start + gap, len(a_list), gap):
            current_value = a_list[idx]
            position = idx
            while position > start and current_value < a_list[position - gap]:
                a_list[position] = a_list[position - gap]
                position -= gap
            a_list[position] = current_value
    
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for i in range(sublist_count):
            gap_insertion_sort(a_list, i, sublist_count)
        sublist_count = sublist_count // 2



if __name__ == '__main__':
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(a_list)
    print(a_list)
