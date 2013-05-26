from linked_list import LinkedList


class AssociativeArray:
    def __init__(self):
        self.items = LinkedList()

    def __unicode__(self):
        s = ''
        for key, value in self.items:
            s += repr(key) + ': ' + repr(value) + ', '
        return '{' + s + '}'

    __repr__ = __unicode__

    def set(self, key, value):
        for i, kv in enumerate(self.items):
            if kv[0] == key:
                l1 = self.items.take(i)
                l2 = self.items.drop(i + 1)
                self.items = l1.concat(l2)
                break
        self.items = self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v
