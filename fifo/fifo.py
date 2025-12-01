from double_linked_list.double_linked_list import DoubleLinkedList


class FIFO:
    def __init__(self):
        self.double_linked_list = DoubleLinkedList()

    def __len__(self):
        return len(self.double_linked_list)

    def enqueue(self, x):
        self.double_linked_list.push_front(x)

    def dequeue(self):
        if self.__len__() == 0:
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.double_linked_list.pop_back()

    def peek(self):
        if self.__len__() == 0:
            raise IndexError("Cannot peek from an empty queue.")
        return self.double_linked_list.tail.data
