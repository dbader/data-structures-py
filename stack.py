from linked_list import LinkedList


class UnderflowException(Exception):
    pass


class Stack:
    def __init__(self):
        self.items = LinkedList()

    def __str__(self):
        return str(self.items)

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
        if self.is_empty:
            raise UnderflowException
        else:
            return self.items.head
