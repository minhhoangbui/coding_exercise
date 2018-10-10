This repository contains my implementation of useful data structures, algorithms, 
games, as well as my solutions to programming puzzles. 

Each item is marked with a difficulty level.
1 - easy
2 - medium
3 - hard

If a file name starts with 'lc', it's a problem from leetcode.com

Written in python2.

Data structures
---------------

### Linked lists

- [x] List class (linked_list.py) - 1
- [x] Remove duplicates (linked_list_algos.py)
- [ ] Find nth last element (linked_list_algos.py)
- [ ] Remove node given only its object (linked_list_algos.py)
- [ ] Sum linked lists with one digit per node (linked_list_algos.py)
- [ ] Find beginning of circle (linked_list_algos.py)

### Trees

- [ ] Binary heap class (binary_heap.py) 
- [x] Binary tree class (binary_tree.py) 
- [ ] Binary search tree class that allows duplicate values (binary_search_tree.py) 
	  BST class inherits binary tree class
- [ ] Red black tree class (red_black_tree.py)
- [ ] B+ tree class (b_tree.py) 
- [ ] Trie class that allows word removal (trie.py) 
- [ ] Check if a binary tree is a binary search tree (binary_tree_algos.py) 
- [ ] Check if a binary tree is balanced (binary_tree_algos.py)
- [ ] Find first common ancestor of two nodes in a binary tree (binary_tree_algos.py)
- [ ] Get all nodes of depth n in a binary tree (binary_tree_algos.py)
- [ ] Given two large trees, check if the first is a subtree of the second (binary_tree_algos.py)
- [ ] Find all sub paths in a binary tree that sum up to x (binary_tree_algos.py)
- [ ] Create a balanced binary search tree from a sorted array (bst_algos.py)

### Graphs

- [ ] Undirected graph class
- [ ] Directed graph class
- [ ] Breadth first search (search.py)
- [ ] Depth first search (search.py)
- [ ] A-star (search.py)

### Stacks and queues

- [x] Queue class (queue.py)
- [ ] Heap priority queue (priority_queue.py)
- [x] Stack class (stack.py)
- [ ] Stack that finds min in O(1) (min_stack.py)
- [x] Solve Hanoi towers using stacks (stack_algos.py)
- [ ] Sort stack using only push, pop, peek and empty (stack_algos.py)
- [ ] Build a queue using two stacks (stack_algos.py)

### Hashing
- [ ] Hash table class

Algorithms
----------

### Sorting and Searching
- [x] Binary search (search.py)
- [x] Sequential search (search.py)
- [x] Bubble sort (sort.py)
- [x] Insertion sort (sort.py)
- [x] Shell sort (sort.py)
- [x] Selection sort (sort.py) 
- [x] Merge sort (sort.py) 
- [ ] Heap sort (sort.py) 
- [x] Quick sort (sort.py) 
- [ ] Counting sort (sort.py) 
- [ ] Radix sort (sort.py)
- [ ] Bucket sort (sort.py)

### Dynamic Programming
- [x] Computing a Fibonacci sequence
- [ ] Find the longest common subsequence between two strings

### Recursion

- [x] Find all permutations of a string
- [x] Find all subsets of a set
- [ ] Find all proper combinations of n parentheses
- [ ] Bucket fill
- [ ] Check if it's possible to make a change with a set of coins
- [ ] Check if it's possible to weight two objects with a set of weights
- [x] Eight queen
- [x] Krap sack
- [x] Minimum coin changing


Programming Puzzles
-------------------

### String Manipulation

- [ ] Check if two strings are anagrams in O(n + m) time (anagrams.py) 
- [ ] Find the longest palindromic substring in O(n^2) time (lc_longest_palindrome.py)
- [x] Check if a string has balanced delimiters in O(n) time (stack_algos.py)
- [ ] Reverse words while maintaining spaces and tabs in O(n) time (reverse_words.py)
- [ ] Longest substring without repeating characters in O(n) time (lc_longest_nonrepeat_substring.py) 
- [ ] Longest contiguous substring of 2 distinct characters in O(n) time (substring_two_chars.py)
- [x] Remove duplicate chars in a string
- [ ] Encode and decode Caesar cipher (caesar.py)
- [ ] Check if a string is a rotation of another

### Mathematical

- [x] Reverse integers (lc_reverse_int.py)
- [x] Sieve of Eratosthenes (sieve_prime.py)
- [x] Two sum in O(n) time (lc_two_sum.py)
	  Given an array of integers, return indices of the two numbers 
	  such that they add up to a specific target.
- [x] Year with maximum population (year_max_pop.py)
	  Given a list of people with their years of birth and death, 
	  find the year with max population
- [x] FizzBuzz (fizzbuzz.py)
- [ ] ZigZag conversion (lc_zigzag_convert.py)
- [ ] Find sum of all subarrays of an array (subarray_sum.py)
- [ ] Add two numbers, each represented by a reverse linked list (lc_add_number_reverse.py)
- [ ] Find the median of two sorted arrays in O(log(m+n)) time (lc_median_arrays.py)
- [ ] Find nth smallest number that can be created using a list of prime factors
- [x] Count occurences of given digit in all numbers up to n
- [ ] Rotate N x N matrix in place
