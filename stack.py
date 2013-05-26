from linked_list import LinkedList


class Stack:
    def __init__(self):
        self.items = LinkedList()

    @property
    def is_empty(self):
        """O(1)"""
        return self.items.is_empty

    def push(self, x):
        """O(1)"""
        self.items = self.items.prepend(x)

    def pop(self):
        """O(1)"""
        x = self.peek()
        self.items = self.items.tail
        return x

    def peek(self):
        """O(1)"""
        return self.items.head
