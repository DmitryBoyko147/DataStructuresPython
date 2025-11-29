import unittest

from binary_heap import BinaryHeap
from vector.vector import Vector


class BinaryHeapTest(unittest.TestCase):
    def test_is_heap(self):
        n = 15
        vector = Vector()
        for i in range(n):
            vector.push_back(i)
        self.assertTrue(BinaryHeap.is_heap(vector))
        vector[0] = n
        self.assertFalse(BinaryHeap.is_heap(vector))

    def test_heapify(self):
        n = 15
        heap = BinaryHeap.heapify(n - i for i in range(n))
        self.assertTrue(BinaryHeap.is_heap(heap.vector))

    def test_push(self):
        n = 15
        heap = BinaryHeap.heapify(i for i in range(n))
        heap.push(0)
        self.assertTrue(BinaryHeap.is_heap(heap.vector))

    def test_pop_min(self):
        n = 15
        heap = BinaryHeap.heapify(n - i - 1 for i in range(n))
        x = heap.pop_min()
        self.assertEqual(x, 0)
        self.assertTrue(BinaryHeap.is_heap(heap.vector))
        with self.assertRaises(IndexError):
            BinaryHeap().pop_min()
        sorted_vector = sorted([i for i in heap.vector])
        binary_heap_sorted_vector = [heap.pop_min() for _ in range(len(heap))]
        self.assertEqual(sorted_vector, binary_heap_sorted_vector)

    def test_push_min(self):
        n = 15
        heap = BinaryHeap.heapify(i for i in range(n))
        self.assertEqual(heap.peek_min(), 0)
        with self.assertRaises(IndexError):
            BinaryHeap().peek_min()

    def test_len(self):
        heap = BinaryHeap()
        self.assertEqual(len(heap), 0)
        heap.push(0)
        heap.push(1)
        self.assertEqual(len(heap), 2)
        heap.peek_min()
        self.assertEqual(len(heap), 2)
        heap.pop_min()
        self.assertEqual(len(heap), 1)


if __name__ == "__main__":
    unittest.main()
