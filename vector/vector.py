class Vector:
    def __init__(self):
        self.capacity = 10
        self.array = [None] * self.capacity
        self.size = 0

    def _extend_array(self):
        old_capacity = self.capacity
        old_array = self.array
        self.capacity = self.capacity * 2
        self.array = [None] * self.capacity
        for i in range(old_capacity):
            self.array[i] = old_array[i]

    def __len__(self):
        return self.size

    def push_back(self, x):
        if self.size == self.capacity:
            self._extend_array()
        self.array[self.size] = x
        self.size += 1

    def push_front(self, x):
        if self.size == self.capacity:
            self._extend_array()
        for i in range(self.size, 0, -1):
            self.array[i] = self.array[i - 1]
        self.array[0] = x
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError("Cannot pop back from an empty array.")
        x = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return x

    def pop_front(self):
        if self.size == 0:
            raise IndexError("Cannot pop front from an empty array.")
        x = self.array[0]
        for i in range(self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return x

    def remove(self, idx):
        if idx >= self.size:
            raise IndexError(
                f"Index {idx} is greater or equal to array's size {self.size}."
            )
        for i in range(idx, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

    def swap_remove(self, idx):
        if idx >= self.size:
            raise IndexError(
                f"Index {idx} is greater or equal to array's size {self.size}."
            )
        self.array[idx] = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1

    def clear(self):
        del self.array
        self = self.__init__()

    def __setitem__(self, idx, x):
        if idx >= self.size:
            raise IndexError(
                f"Index {idx} is greater or equal to array's size {self.size}."
            )
        self.array[idx] = x

    def __getitem__(self, idx):
        if idx >= self.size:
            raise IndexError(
                f"Index {idx} is greater or equal to array's size {self.size}."
            )
        return self.array[idx]

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current == self.size:
            raise StopIteration
        else:
            x = self.array[self.current]
            self.current += 1
            return x
