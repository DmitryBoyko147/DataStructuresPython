class Stack:
    def __init__(self):
        self.size = 0
        self.array = []

    def push(self, x):
        self.array.append(x)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Cannot pop from an empty stack.")
        self.size -= 1
        return self.array.pop()

    def top(self):
        if self.size == 0:
            raise IndexError("Cannot top from an empty stack.")
        return self.array[-1]

    def __len__(self):
        return self.size
