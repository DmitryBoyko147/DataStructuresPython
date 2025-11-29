class DSU:
    def __init__(self, n: int):
        self.n = n
        self.array = list(range(n))
        self.ranks = [1] * n

    def find(self, x: int) -> int:
        stack = [(x, 0)]
        root = x
        while stack:
            x, status = stack.pop()
            if self.array[x] == x:
                root = x
            elif status == 1:
                self.array[x] = root
            else:
                stack.append((x, 1))
                stack.append((self.array[x], 0))
        return root

    def union(self, x: int, y: int) -> int:
        x_root = self.find(x)
        y_root = self.find(y)
        if self.ranks[x_root] < self.ranks[y_root]:
            x_root, y_root = y_root, x_root
        self.array[y_root] = x_root
        self.ranks[x_root] = max(self.ranks[x_root], self.ranks[y_root] + 1)
        return x_root

    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
