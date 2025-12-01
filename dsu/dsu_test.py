import unittest

from dsu import DSU


class DSUTest(unittest.TestCase):
    @staticmethod
    def create_dsu() -> DSU:
        n = 10
        dsu = DSU(n)
        dsu.union(1, 2)
        dsu.union(2, 3)
        dsu.union(4, 5)
        dsu.union(5, 6)
        dsu.union(3, 6)
        return dsu

    def test_find(self):
        dsu = self.create_dsu()
        self.assertEqual(dsu.array[4], 1)
        self.assertEqual(dsu.array[6], 4)
        self.assertEqual(dsu.find(6), 1)
        self.assertEqual(dsu.array[6], 1)
        self.assertEqual(dsu.array[5], 4)

    def test_union(self):
        dsu = self.create_dsu()
        self.assertEqual(dsu.ranks[1], 3)
        self.assertEqual(dsu.ranks[4], 2)
        self.assertEqual(dsu.find(4), 1)
        self.assertEqual(dsu.find(3), dsu.find(6))

    def test_is_same(self):
        dsu = self.create_dsu()
        self.assertEqual(dsu.find(3), dsu.find(5))
        self.assertNotEqual(dsu.find(6), dsu.find(0))


if __name__ == "__main__":
    unittest.main()
