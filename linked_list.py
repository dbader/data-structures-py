#pylint: disable=W0142, R0924


class LinkedList:
    Nil = None

    def __init__(self, *xs):
        """Convenience constructor to create a list from a variable
        number of arguments.
        """
        def make(*xs):
            if not xs:
                return LinkedList.Nil
            else:
                return LinkedList.cons(xs[0], make(*xs[1:]))
        self.items = make(*xs)

    @staticmethod
    def from_cons(xs):
        l = LinkedList()
        l.items = xs
        return l

    @staticmethod
    def cons(x, xs=Nil):
        return (x, xs)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.items == other.items

    def __unicode__(self):
        def stringify(xs):
            if xs.is_empty:
                return ''
            elif xs.tail.is_empty:
                return str(xs.head)
            else:
                return str(xs.head) + ', ' + stringify(xs.tail)
        return '[' + stringify(self) + ']'

    __repr__ = __unicode__

    def __getitem__(self, index):
        return self.apply(index)

    def __len__(self):
        return self.length

    def __iter__(self):
        iter_list = self
        while not iter_list.is_empty:
            yield iter_list.head
            iter_list = iter_list.tail

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

    def prepend(self, x):
        return LinkedList.from_cons(LinkedList.cons(x, self.items))

    def append(self, x):
        def __ap(xs, y):
            if xs == LinkedList.Nil:
                return LinkedList.cons(y)
            else:
                return LinkedList.cons(xs[0], __ap(xs[1], y))
        return self.from_cons(__ap(self.items, x))

    def concat(self, xs):
        def __cc(xs, ys):
            if xs == LinkedList.Nil:
                return ys
            else:
                return LinkedList.cons(xs[0], __cc(xs[1], ys))
        return self.from_cons(__cc(self.items, xs.items))

    def take(self, n):
        def __tt(n, xs):
            if n == 0:
                return LinkedList.Nil
            else:
                return LinkedList.cons(xs[0], __tt(n - 1, xs[1]))
        return self.from_cons(__tt(n, self.items))

    def drop(self, n):
        if n == 0:
            return self
        else:
            return self.tail.drop(n - 1)

    def apply(self, index):
        return self.drop(index).head
