'''
An implementation of Queue data structure
'''
from __future__ import print_function

class Queue(object):
    def __init__(self):
        self.queue = []
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return self.size() == 0
    
    def enqueue(self, value):
        return self.queue.insert(0, value)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop()

def createQueue(elements):
    my_queue = Queue()
    for i in elements:
        my_queue.enqueue(i)
    return my_queue

if __name__ == '__main__':
    queue = Queue()
    print(queue.is_empty())
    queue.enqueue(4)
    queue.enqueue('dog')
    queue.enqueue(True)
    print(queue.size())
    print(queue.is_empty())
    queue.enqueue(8.4)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.size())

