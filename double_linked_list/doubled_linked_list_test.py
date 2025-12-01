import unittest

from double_linked_list import DoubleLinkedList


class DoubleLinkedListTest(unittest.TestCase):
    def test_len(self):
        n = 10
        dll = DoubleLinkedList()
        self.assertEqual(len(dll), 0)
        for i in range(n):
            dll.push_back(i)
        self.assertEqual(len(dll), n)

    def test_find(self):
        n = 10
        dll = DoubleLinkedList()
        self.assertIsNone(dll.find(5))
        for i in range(n):
            dll.push_back(i)
        self.assertEqual(dll.find(5).data, 5)

    def test_push_front(self):
        dll = DoubleLinkedList()
        dll.push_front(5)
        self.assertEqual(dll.head, dll.tail)
        dll.push_front(10)
        self.assertEqual(dll.head.next_, dll.tail)
        self.assertEqual(dll.head.data, 10)
        self.assertEqual(dll.head, dll.tail.prev)
        self.assertEqual(dll.tail.data, 5)
        self.assertEqual(len(dll), 2)

    def test_push_back(self):
        dll = DoubleLinkedList()
        dll.push_back(5)
        self.assertEqual(dll.head, dll.tail)
        dll.push_back(10)
        self.assertEqual(dll.head.next_, dll.tail)
        self.assertEqual(dll.head.data, 5)
        self.assertEqual(dll.head, dll.tail.prev)
        self.assertEqual(dll.tail.data, 10)
        self.assertEqual(len(dll), 2)

    def test_pop_front(self):
        dll = DoubleLinkedList()
        with self.assertRaises(IndexError):
            dll.pop_front()
        dll.push_front(5)
        self.assertEqual(len(dll), 1)
        dll.pop_front()
        self.assertEqual(len(dll), 0)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        dll.push_front(5)
        dll.push_front(10)
        dll.pop_front()
        self.assertEqual(dll.head, dll.tail)

    def test_pop_back(self):
        dll = DoubleLinkedList()
        with self.assertRaises(IndexError):
            dll.pop_back()
        dll.push_front(5)
        self.assertEqual(len(dll), 1)
        dll.pop_back()
        self.assertEqual(len(dll), 0)
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        dll.push_front(5)
        dll.push_front(10)
        dll.pop_back()
        self.assertEqual(dll.head, dll.tail)

    def test_insert(self):
        dll = DoubleLinkedList()
        node = dll.push_front(5)
        dll.insert(10, node)
        self.assertEqual(node.next_, dll.tail)
        self.assertEqual(node, node.next_.prev)
        dll.insert(15, node)
        self.assertEqual(node.next_.data, 15)
        self.assertEqual(node, node.next_.prev)
        self.assertEqual(node.next_.next_.prev, node.next_)
        self.assertEqual([5, 15, 10], [node.data for node in dll])

    def test_remove(self):
        dll = DoubleLinkedList()
        dll.push_front(5)
        dll.remove(10)
        self.assertEqual(len(dll), 1)
        self.assertIsNotNone(dll.find(5))
        dll.remove(5)
        self.assertEqual(len(dll), 0)
        self.assertIsNone(dll.find(5))
        dll.push_front(5)
        dll.push_front(5)
        dll.remove(5)
        self.assertIsNotNone(dll.find(5))


if __name__ == "__main__":
    unittest.main()
