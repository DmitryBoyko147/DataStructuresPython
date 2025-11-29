import unittest

from leftist_heap import LeftistHeap


class LeftistHeapTest(unittest.TestCase):
    def test_heapify(self):
        n = 15
        heap = LeftistHeap.heapify([i for i in range(n)])
        self.assertTrue(LeftistHeap.is_heap(heap))
        heap.data = n
        self.assertFalse(LeftistHeap.is_heap(heap))
        self.assertEqual(len(heap), n)

    def test_meld(self):
        n = 15
        h1 = LeftistHeap.heapify([i for i in range(n)])
        h2 = LeftistHeap.heapify([n - i - 1 for i in range(n)])
        h1.meld(h2)
        self.assertTrue(LeftistHeap.is_heap(h1))
        self.assertTrue(LeftistHeap.is_heap(h2))
        self.assertEqual(len(h1), 2 * n)
        self.assertEqual(len(h2), 0)
        h2.meld(h1)
        self.assertTrue(LeftistHeap.is_heap(h1))
        self.assertTrue(LeftistHeap.is_heap(h2))
        self.assertEqual(len(h1), 0)
        self.assertEqual(len(h2), 2 * n)
        h1 = LeftistHeap()
        h2 = LeftistHeap()
        h1.meld(h2)
        self.assertTrue(LeftistHeap.is_heap(h1))
        self.assertTrue(LeftistHeap.is_heap(h2))
        self.assertEqual(len(h1), 0)
        self.assertEqual(len(h2), 0)

    def test_push(self):
        heap = LeftistHeap()
        heap.push(0)
        self.assertEqual(len(heap), 1)
        self.assertEqual(heap.data, 0)
        heap.push(-1)
        heap.push(1)
        self.assertEqual(len(heap), 3)
        self.assertEqual(heap.data, -1)

    def test_pop_min(self):
        with self.assertRaises(IndexError):
            LeftistHeap().pop_min()
        n = 15
        heap = LeftistHeap.heapify([i for i in range(n)])
        self.assertEqual(
            [i for i in range(n)], [heap.pop_min() for _ in range(len(heap))]
        )
        self.assertEqual(len(heap), 0)

    def test_peek_min(self):
        with self.assertRaises(IndexError):
            LeftistHeap().pop_min()
        n = 15
        heap = LeftistHeap.heapify([i for i in range(n)])
        self.assertEqual(heap.peek_min(), 0)
        self.assertEqual(len(heap), n)


if __name__ == "__main__":
    unittest.main()
