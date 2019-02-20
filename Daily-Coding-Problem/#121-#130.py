'''Solve Daily Coding Problems from #121-#130'''
from outils import Stack, SinglyLinkedList, SNode


def prob_122(matrix):
    '''
    This question was asked by Zillow.

    You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start 
    at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by 
    the bottom right corner.

    For example, in this matrix

    0 3 1 1
    2 0 0 4
    1 5 3 1

    The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
    '''
    M = len(matrix)
    N = len(matrix[0])

    coins = [[0] * (N + 1)] * (M + 1)
    for i in range(M):
        for j in range(N):
            coins[M - 1 - i][N - 1 - j] = matrix[M - 1 - i][N - 1 - j] \
                + max(coins[M - i][N - 1 - j], coins[M - i - 1][N - j])
    return coins[0][0]

def prob_123(string):
    '''
    Given a string, return whether it represents a number. Here are the different kinds of numbers:

        "10", a positive integer
        "-10", a negative integer
        "10.1", a positive real number
        "-10.1", a negative real number
        "1e5", a number in scientific notation
    And here are examples of non-numbers:

        "a"
        "x 1"
        "a -2"
        "-"
    '''
    pass

def prob_126(a_list, k):
    '''
    Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by 
    two becomes [3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of the list. How many 
    swap or move operations do you need?
    '''
    temp = []
    for _ in range(k):
        temp.append(a_list.pop(0))
    while temp:
        a_list.append(temp.pop(0))
    return a_list

def prob_127(list1, list2):
    '''
    For example, the following linked list:

    1 -> 2 -> 3 -> 4 -> 5
    is the number 54321.

    Given two linked lists in this format, return their sum in the same linked list format.

    For example, given

    9 -> 9
    5 -> 2
    return 124 (99 + 25) as:

    4 -> 2 -> 1
    '''
    list1 = list1.print_list()
    list2 = list2.print_list()
    list1.reverse()
    list2.reverse()
    list1 = [str(i) for i in list1]
    list2 = [str(j) for j in list2]
    num1 = int(''.join(list1))
    num2 = int(''.join(list2))
    num = num1 + num2
    num = list(str(num))
    node = SNode(int(num[0]))
    linked_list = SinglyLinkedList(node)
    for i in num[1:]:
        linked_list.insert_head(int(i))
    return linked_list

def prob_128():
    '''
    The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.

    All the disks start off on the first rod in a stack. They are ordered by size, with the largest disk 
    on the bottom and the smallest one at the top.

    The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:

    You can only move one disk at a time.
    A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
    You cannot place a larger disk on top of a smaller disk.
    Write a function that prints out all the steps necessary to complete the Tower of Hanoi. You should assume 
    that the rods are numbered, with the first rod being 1, the second (auxiliary) rod being 2, and the last 
    (goal) rod being 3.

    For example, with n = 3, we can do this in 7 moves:

    Move 1 to 3
    Move 1 to 2
    Move 3 to 2
    Move 1 to 3
    Move 2 to 1
    Move 2 to 3
    Move 1 to 3
    '''

    class HNTower:
        def __init__(self):
            self.stacks = [Stack(), Stack(), Stack()]
        
        def __call__(self, num_disks, src, dst):
            temp = [0, 1, 2]
            temp.remove(dst)
            temp.remove(src)
            aux = temp[0]

            for i in range(num_disks):
                self.stacks[src].push(i)
            
            self._move_tower(num_disks, src, aux, dst)
        
        def _move_disk(self, src, dst):
            print('Move %d to %d'%(src+1, dst+1))
            self.stacks[dst].push(self.stacks[src].pop())
        
        def _move_tower(self, num_disks, src, aux, dst):
            if num_disks == 1:
                self._move_disk(src, dst)
            else:
                self._move_tower(num_disks - 1, src, dst, aux)
                self._move_disk(src, dst)
                self._move_tower(num_disks - 1, aux, src, dst)
    
    hntower = HNTower()
    hntower(3, 0, 2)

def prob_129(n):
    '''
    Given a real number n, find the square root of n. For example, given n = 9, return 3.
    '''
    import math
    return math.sqrt(n)


if __name__ == '__main__':
    node1 = SNode(9)
    list1 = SinglyLinkedList(node1)
    list1.insert_head(9)

    node2 = SNode(2)
    list2 = SinglyLinkedList(node2)
    list2.insert_head(5)

    ll = prob_127(list1, list2)
    print ll.print_list()
