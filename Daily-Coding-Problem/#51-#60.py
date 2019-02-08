'''Solve Daily Coding Problems from #51-#60'''

from outils import Stack

def prob_52():
    '''
    Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, 
    and contain the following methods:

    - set(key, value): sets key to value. If there are already n items in the cache and we are adding a 
    new item, then it should also remove the least recently used item.
    - get(key): gets the value at key. If no such key exists, return null.

    Each operation should run in O(1) time.
    '''
    from collections import OrderedDict
    class LRUCache(object):
        def __init__(self, size):
            self.cache = OrderedDict()
            self.size = size
            self.currentSize = 0
        
        def set(self, key, value):
            if self.currentSize < self.size:
                self.cache[key] = value
                self.currentSize += 1
            else:
                self.cache = OrderedDict(self.cache.items()[1:])
                self.cache[key] = value
        
        def get(self, key):
            try:
                return self.cache[key]
            except KeyError:
                return None

def prob_53():
    '''
    Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure 
    with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
    '''
    class Queue(object):
        def __init__(self):
            self._stack_1 = Stack()
            self._stack_2 = Stack()
        
        def __len__(self):
            return len(self._stack_1) + len(self._stack_2)
        
        def enqueue(self, value):
            self._stack_1.push(value)
        
        def dequeue(self):
            if self._stack_2.is_empty():
                while len(self._stack_1):
                    self._stack_2.push(self._stack_1.pop())
            return self._stack_2.pop()
    
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print queue.dequeue()
    print len(queue)
    
def prob_55():
    '''
    Implement a URL shortener with the following methods:

    - shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
    - restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
    Hint: What if we enter the same URL twice?
    '''
    import random, string
    class URLShortener(object):
        def __init__(self):
            self.urlDict = {}
        
        def shorten(self, url):
            if url in self.urlDict:
                return self.urlDict[url]
            else:
                self.urlDict[url] = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))

        def restore(self, shortener):
            for key, val in self.urlDict.iteritems():
                if val == shortener:
                    return key

def prob_56():
    '''
    Given an undirected graph represented as an adjacency matrix and an integer k, write a function 
    to determine whether each vertex in the graph can be colored such that no two adjacent vertices share 
    the same color using at most k colors.
    '''
    pass 

def prob_57(string):
    '''
    Given a string s and an integer k, break up the string into multiple texts such that each text has a length of 
    k or less. You must break it up so that words don't break across lines. If there's no way to break the text up, 
    then return null.

    You can assume that there are no spaces at the ends of the string and that there is exactly one space between 
    each word.

    For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: 
    ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
    '''
    pass

def prob_58():
    '''
    An sorted array of integers was rotated an unknown number of times.

    Given such an array, find the index of the element in the array in faster than linear time. If 
    the element doesn't exist in the array, return null.

    For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

    You can assume all the integers in the array are unique.
    '''
    pass

def prob_60(a_list):
    '''
    Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

    For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up 
    into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

    Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets 
    that add up to the same sum.
    '''
    pass

if __name__ == '__main__':
    prob_53()
