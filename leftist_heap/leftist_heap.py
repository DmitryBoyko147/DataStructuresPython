from copy import copy

from fifo.fifo import FIFO


class LeftistHeap:
    @staticmethod
    def heapify(iterable):
        heaps = FIFO()
        for x in iterable:
            heap = LeftistHeap()
            heap._push_first(x)
            heaps.enqueue(heap)
        while len(heaps) > 1:
            h1 = heaps.dequeue()
            h2 = heaps.dequeue()
            heaps.enqueue(h1.meld(h2))
        return heaps.dequeue()

    @staticmethod
    def _meld(x, y):
        if x is None or x.size == 0:
            return copy(y)
        if y is None or y.size == 0:
            return copy(x)
        if x.data > y.data:
            x, y = y, x
        heap = LeftistHeap()
        heap.data = x.data
        heap.left = x.left
        heap.right = LeftistHeap._meld(x.right, y)
        if heap.left is None or heap.left.dist < heap.right.dist:
            heap.left, heap.right = heap.right, heap.left
        heap.size = 1 + heap.left.size + (0 if heap.right is None else heap.right.size)
        heap.dist = 1 + (0 if heap.right is None else heap.right.dist)
        return heap

    @staticmethod
    def is_heap(heap):
        if heap.left is None and heap.right is None:
            return True
        if heap.left is None and heap.right is not None:
            return False
        if heap.data > heap.left.data:
            return False
        if not LeftistHeap.is_heap(heap.left):
            return False
        if heap.right is not None:
            if heap.data > heap.right.data:
                return False
            if not LeftistHeap.is_heap(heap.right):
                return False
            if heap.left.dist < heap.right.dist:
                return False
        return True

    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.size = 0
        self.dist = 0

    def _push_first(self, x):
        if self.size > 0:
            raise ValueError("Can only push first to an empty heap.")
        self.data = x
        self.size = 1
        self.dist = 1

    def _clear(self):
        self = self.__init__()

    def __len__(self):
        return self.size

    def meld(self, other):
        heap = LeftistHeap._meld(self, other)
        self.data = heap.data
        self.left = heap.left
        self.right = heap.right
        self.size = heap.size
        self.dist = heap.dist
        other._clear()
        return self

    def push(self, x):
        if self.size == 0:
            self._push_first(x)
        else:
            heap = LeftistHeap()
            heap._push_first(x)
            self.meld(heap)

    def pop_min(self):
        if self.size == 0:
            raise IndexError("Cannot peek min from an empty heap.")
        x = self.data
        if self.left is None:
            self._clear()
        else:
            heap = LeftistHeap._meld(self.left, self.right)
            self.data = heap.data
            self.left = heap.left
            self.right = heap.right
            self.size = heap.size
            self.dist = heap.dist
        return x

    def peek_min(self):
        if self.size == 0:
            raise IndexError("Cannot peek min from an empty heap.")
        return self.data
