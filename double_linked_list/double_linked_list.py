class DoubleLinkedList:
    class Node:
        def __init__(self, data, prev=None, next_=None):
            self.data = data
            self.prev = prev
            self.next_ = next_

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def find(self, x) -> Node:
        node = self.head
        while node is not None and node.data != x:
            node = node.next_
        return node

    def push_front(self, x) -> Node:
        node = self.Node(x)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next_ = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
        return node

    def push_back(self, x) -> Node:
        node = self.Node(x)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next_ = node
            self.tail = node
        self.size += 1
        return node

    def pop_front(self):
        if self.size == 0:
            raise IndexError("Cannot pop front from an empty list.")
        node = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_
            self.head.prev = None
        self.size -= 1
        return node.data

    def pop_back(self):
        if self.size == 0:
            raise IndexError("Cannot pop back from an empty list.")
        node = self.tail
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next_ = None
        self.size -= 1
        return node.data

    def insert(self, x, node):
        new_node = self.Node(x)
        new_node.next_ = node.next_
        if node.next_ is None:
            self.tail = new_node
        else:
            node.next_.prev = new_node
        new_node.prev = node
        node.next_ = new_node

    def remove(self, x):
        node = self.find(x)
        if node is None:
            return
        if node == self.head:
            self.pop_front()
        elif node == self.tail:
            self.pop_back()
        else:
            node.prev.next_ = node.next_
            node.next_.prev = node.prev
            self.size -= 1

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            node = self.current
            self.current = self.current.next_
            return node
