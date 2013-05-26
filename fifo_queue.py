from linked_list import LinkedList


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
        """O(n)"""
        self.items = self.items.append(x)

    def dequeue(self):
        """O(1)"""
        if self.is_empty:
            raise UnderflowException
        else:
            x = self.items.head
            self.items = self.items.drop(1)
            return x
