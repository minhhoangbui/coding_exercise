'''
Some popular algorithm with LinkedList
'''
from linked_list import LinkedList

class AdvancedLinkedList(LinkedList):
    def __init__(self, head=None):
        super(AdvancedLinkedList, self).__init__(head=head)
    
    def removeDuplicates(self):
        current = second = self.head
        while current:
            while second and second.get_next():
                if second.get_next().value == current.value:
                    second.next_node = second.get_next().get_next()
                else:
                    second = second.get_next()
            current = second = current.get_next()

def creatList(elements):
    my_list = AdvancedLinkedList()
    for i in elements:
        my_list.insert(i)
    return my_list

if __name__ == '__main__':
    my_list = creatList([5, 8, 9, 8, 9, 3])
    my_list.removeDuplicates()
    my_list.print_list()
