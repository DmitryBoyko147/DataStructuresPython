import unittest
from typing import Tuple

from stack import Stack


class StackTest(unittest.TestCase):
    @staticmethod
    def create_stack() -> Tuple[Stack, int]:
        n = 5
        stack = Stack()
        for i in range(n):
            stack.push(i * i)
        return stack, n

    def test_len(self):
        self.assertEqual(len(Stack()), 0)
        stack, n = self.create_stack()
        self.assertEqual(len(stack), n)

    def test_push(self):
        stack, n = self.create_stack()
        self.assertEqual(stack.array, [i * i for i in range(n)])

    def test_top(self):
        stack, n = self.create_stack()
        self.assertEqual(stack.top(), (n - 1) * (n - 1))
        stack, _ = self.create_stack()
        old_len = len(stack)
        stack.top()
        new_len = len(stack)
        self.assertEqual(old_len, new_len)
        with self.assertRaises(IndexError):
            Stack().top()

    def test_pop(self):
        stack, n = self.create_stack()
        self.assertEqual(stack.pop(), (n - 1) * (n - 1))
        stack, n = self.create_stack()
        old_len = len(stack)
        stack.pop()
        new_len = len(stack)
        self.assertEqual(old_len - 1, new_len)
        with self.assertRaises(IndexError):
            Stack().pop()
        self.assertEqual(
            sorted(stack.array, reverse=True), [stack.pop() for _ in range(len(stack))]
        )


if __name__ == "__main__":
    unittest.main()
