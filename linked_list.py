#pylint: disable=W0142


class LinkedList:
    Nil = None

    def __init__(self, *xs):
        self.items = self.lst(*xs)

    @staticmethod
    def from_cons(xs):
        l = LinkedList()
        l.items = xs
        return l

    @staticmethod
    def cons(x, xs=Nil):
        return (x, xs)

    @staticmethod
    def lst(*xs):
        if not xs:
            return LinkedList.Nil
        else:
            return LinkedList.cons(xs[0], LinkedList.lst(*xs[1:]))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.items == other.items

    @property
    def head(self):
        return self.items[0]

    @property
    def tail(self):
        return LinkedList.from_cons(self.items[1])

    @property
    def is_empty(self):
        return self.items == LinkedList.Nil

    @property
    def length(self):
        if self.is_empty:
            return 0
        else:
            return 1 + self.tail.length
