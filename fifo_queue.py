from linked_list import LinkedList
from stack import Stack


class UnderflowException(Exception):
    pass


class Queue:
    def __init__(self):
        self.items = LinkedList()

    @property
    def is_empty(self):
        """O(1)"""
        return self.items.is_empty

    def enqueue(self, x):
        """O(n) --> should be O(1)"""
        self.items = self.items.append(x)

    def dequeue(self):
        """O(1)"""
        if self.is_empty:
            raise UnderflowException
        else:
            x = self.items.head
            self.items = self.items.drop(1)
            return x


class StackQueue:
    """A queue implemented using two stacks"""
    def __init__(self):
        self.newest = Stack()  # newest elements on top
        self.oldest = Stack()  # oldest elements on top

    @property
    def is_empty(self):
        return self.newest.is_empty and self.oldest.is_empty

    def enqueue(self, x):
        self.newest.push(x)

    def dequeue(self):
        if self.is_empty:
            raise UnderflowException
        if not self.oldest.is_empty:
            return self.oldest.pop()
        while not self.newest.is_empty:
            self.oldest.push(self.newest.pop())
        return self.oldest.pop()
