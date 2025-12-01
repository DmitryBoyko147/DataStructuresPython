from vector.vector import Vector


class BinaryHeap:
    @staticmethod
    def heapify(iterable):
        vector = Vector()
        for i in iterable:
            vector.push_back(i)
        heap = BinaryHeap()
        heap.vector = vector
        for i in range(len(vector) - 1, -1, -1):
            heap._sift_down(i)
        return heap

    @staticmethod
    def is_heap(vector: Vector, idx: int = 0) -> bool:
        if idx >= len(vector):
            return True
        if 2 * idx + 1 < len(vector) and vector[idx] > vector[2 * idx + 1]:
            return False
        if 2 * idx + 2 < len(vector) and vector[idx] > vector[2 * idx + 2]:
            return False
        return BinaryHeap.is_heap(vector, 2 * idx + 1) and BinaryHeap.is_heap(
            vector, 2 * idx + 2
        )

    def __init__(self):
        self.vector = Vector()

    def _sift_up(self, idx):
        while idx != 0 and self.vector[idx] < self.vector[(idx - 1) // 2]:
            self.vector[idx], self.vector[(idx - 1) // 2] = (
                self.vector[(idx - 1) // 2],
                self.vector[idx],
            )
            idx = (idx - 1) // 2

    def _sift_down(self, idx):
        while (
            2 * idx + 1 < len(self.vector)
            and self.vector[idx] > self.vector[2 * idx + 1]
            or 2 * idx + 2 < len(self.vector)
            and self.vector[idx] > self.vector[2 * idx + 2]
        ):
            if 2 * idx + 2 < len(self.vector):
                if self.vector[2 * idx + 1] < self.vector[2 * idx + 2]:
                    self.vector[idx], self.vector[2 * idx + 1] = (
                        self.vector[2 * idx + 1],
                        self.vector[idx],
                    )
                    idx = 2 * idx + 1
                else:
                    self.vector[idx], self.vector[2 * idx + 2] = (
                        self.vector[2 * idx + 2],
                        self.vector[idx],
                    )
                    idx = 2 * idx + 2
            else:
                self.vector[idx], self.vector[2 * idx + 1] = (
                    self.vector[2 * idx + 1],
                    self.vector[idx],
                )
                idx = 2 * idx + 1

    def __len__(self):
        return len(self.vector)

    def push(self, x):
        self.vector.push_back(x)
        self._sift_up(len(self.vector) - 1)

    def pop_min(self):
        if len(self.vector) == 0:
            raise IndexError("Cannot pop min from an empty heap.")
        x = self.vector[0]
        self.vector.swap_remove(0)
        self._sift_down(0)
        return x

    def peek_min(self):
        if len(self.vector) == 0:
            raise IndexError("Cannot peek min from an empty heap.")
        return self.vector[0]
