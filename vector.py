#pylint: disable=R0924


class Vector:
    def __init__(self, capacity=0):
        self.items = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def __getitem__(self, index):
        assert 0 <= index < self.size
        return self.items[index]

    def __setitem__(self, index, x):
        assert 0 <= index < self.size
        self.items[index] = x

    @property
    def length(self):
        return self.size

    def append(self, x):
        assert 0 <= self.size <= self.capacity
        if self.size >= self.capacity - 1:
            self.resize(self.capacity + self.capacity // 8 + 3)
        self.items[self.size] = x
        self.size += 1

    def resize(self, capacity):
        assert capacity >= self.size
        old_items = self.items
        self.capacity = capacity
        self.items = [None] * capacity
        for i in range(self.size):
            self.items[i] = old_items[i]

    def delete(self, index):
        for i in range(index, self.length - index):
            self.items[i] = self.items[i+1]
        self.size -= 1
        if self.size < self.capacity // 2:
            self.resize(self.size + self.size // 8 + 3)
