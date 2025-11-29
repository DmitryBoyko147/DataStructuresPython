import unittest
from typing import Tuple

from vector import Vector


class TestVector(unittest.TestCase):
    @staticmethod
    def create_vector(push_back: bool = True) -> Tuple[Vector, int]:
        n = 10
        vector = Vector()
        for i in range(n):
            if push_back:
                vector.push_back(i)
            else:
                vector.push_front(i)
        return vector, n

    def test_len(self):
        self.assertEqual(len(Vector()), 0)
        vector, n = self.create_vector()
        self.assertEqual(len(vector), n)

    def test_push_back(self):
        vector, n = self.create_vector()
        self.assertEqual([i for i in range(n)], vector.array)
        self.assertEqual(len(vector), n)
        old_capacity = vector.capacity
        vector.push_back(n)
        new_capacity = vector.capacity
        self.assertEqual(old_capacity * 2, new_capacity)

    def test_push_front(self):
        vector, n = self.create_vector(push_back=False)
        self.assertEqual([n - i - 1 for i in range(n)], vector.array)
        self.assertEqual(len(vector), n)
        old_capacity = vector.capacity
        vector.push_front(n)
        new_capacity = vector.capacity
        self.assertEqual(old_capacity * 2, new_capacity)

    def test_pop_back(self):
        with self.assertRaises(IndexError):
            Vector().pop_back()
        vector, n = self.create_vector()
        self.assertEqual(vector.pop_back(), n - 1)
        self.assertEqual(len(vector), n - 1)
        self.assertEqual([i for i in range(n - 1)] + [None], vector.array)

    def test_pop_front(self):
        with self.assertRaises(IndexError):
            Vector().pop_front()
        vector, n = self.create_vector()
        self.assertEqual(vector.pop_front(), 0)
        self.assertEqual(len(vector), n - 1)
        self.assertEqual([i for i in range(1, n)] + [None], vector.array)

    def test_remove(self):
        vector, n = self.create_vector()
        with self.assertRaises(IndexError):
            vector.remove(n)
        vector.remove(5)
        self.assertEqual([i for i in range(n) if i != 5] + [None], vector.array)
        self.assertEqual(len(vector), n - 1)

    def test_swap_remove(self):
        vector, n = self.create_vector()
        with self.assertRaises(IndexError):
            vector.swap_remove(n)
        vector.swap_remove(5)
        self.assertEqual(
            [i for i in range(5)] + [n - 1] + [i for i in range(6, n - 1)] + [None],
            vector.array,
        )
        self.assertEqual(len(vector), n - 1)

    def test_clear(self):
        vector, n = self.create_vector()
        self.assertNotEqual(len(vector), 0)
        vector.clear()
        self.assertEqual(len(vector), 0)


if __name__ == "__main__":
    unittest.main()
