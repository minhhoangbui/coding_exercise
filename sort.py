'''
Implementation of sorting techniques in Python 2
'''
from __future__ import print_function

def bubble_sort(a_list):
    '''
    Push the biggest element to the end of the list, it is like the bubble rises from the bottom to the top
    Complexity: O(n)
    It compares the elements from the start to the next-to-end to its follower and exchanges their position if the superiority exists
    '''
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
                a_list[i + 1] = temp
        pass_num -= 1

def selection_sort(a_list):
    '''
    For each pass through the list, it will find the index with the biggest value and move them to the end of the sublist in each pass
    '''
    for slot in range(len(a_list) - 1, 0, -1):
        max_pos = 0
        for loc in range(1, slot + 1):
            if a_list[loc] > a_list[max_pos]:
                max_pos = loc
        temp = a_list[slot]
        a_list[slot] = a_list[max_pos]
        a_list[max_pos] = temp

def insertion_sort(a_list):
    '''
    For all elements except the first one, the algo will compare each of them to the their precedences and move the precedeces if necessary
    It will keep the sorted sublist in the lower position.
    '''
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

def merge_sort(a_list):
    print('Splitting', a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        print(left_half, right_half)

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1
    print('Merging', a_list)


def quick_sort(a_list):
    
    def _quick_sort(a_list, first, last):
        if first <  last:
            split_point = partition(a_list, first, last)

            _quick_sort(a_list, first, split_point - 1)
            _quick_sort(a_list, split_point + 1, last)
    
    def partition(a_list, first, last):
        pivot_value = a_list[first]
        left = first + 1
        right = last 
        done = False
        
        while not done:
            while a_list[left] <= pivot_value and left <= right:
                left += 1
            while a_list[right] >= pivot_value and left <= right:
                right -= 1
            if left > right:
                done = True
            else:
                temp = a_list[left]
                a_list[left] = a_list[right]
                a_list[right] = temp
        
        temp = a_list[right]
        a_list[right] = a_list[first]
        a_list[first] = temp
        return right
    
    _quick_sort(a_list, 0, len(a_list) - 1)
    
def counting_sort(a_list):
    a_min = min(a_list)
    a_max = max(a_list)
    ranges = list(range(a_min, a_max + 1))
    occurence = []
    pos = []
    result = [None] * len(a_list)
    for element in ranges:
        occurence.append(a_list.count(element))
    for idx, val in enumerate(occurence):
        pos.append(sum(occurence[:idx+1]))
    pos.insert(0, 0)
    pos = pos[:len(ranges)]
    for i, j in zip(pos, ranges):
        result[i:] = [j] * (len(a_list) - i)
    print(result)

    

if __name__ == '__main__':
    a_list = [1, 0, 3, 1, 3, 1]
    counting_sort(a_list)
