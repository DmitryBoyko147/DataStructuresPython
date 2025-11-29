import unittest
from typing import Tuple

from fifo import FIFO


class FifoTest(unittest.TestCase):
    @staticmethod
    def create_fifo() -> Tuple[FIFO, int]:
        n = 10
        fifo = FIFO()
        for i in range(n):
            fifo.enqueue(i)
        return fifo, n

    def test_len(self):
        fifo, n = self.create_fifo()
        self.assertEqual(len(FIFO()), 0)
        self.assertEqual(len(fifo), n)

    def test_enqueue(self):
        fifo, n = self.create_fifo()
        self.assertEqual(
            [n - i - 1 for i in range(n)],
            [node.data for node in fifo.double_linked_list],
        )

    def test_deque(self):
        fifo, n = self.create_fifo()
        with self.assertRaises(IndexError):
            FIFO().dequeue()
        self.assertEqual(fifo.dequeue(), 0)
        self.assertEqual(len(fifo), n - 1)
        self.assertEqual(
            [i for i in range(1, n)], [fifo.dequeue() for _ in range(len(fifo))]
        )
        self.assertEqual(len(fifo), 0)

    def test_peek(self):
        fifo, n = self.create_fifo()
        with self.assertRaises(IndexError):
            FIFO().peek()
        self.assertEqual(fifo.peek(), 0)
        self.assertEqual(len(fifo), n)


if __name__ == "__main__":
    unittest.main()
