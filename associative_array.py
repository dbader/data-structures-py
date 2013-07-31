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

    def put(self, key, value):
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


class HashMap:
    def __init__(self):
        self.buckets = [list() for _ in range(64)]

    def __unicode__(self):
        def flattened(xs):
            return (item for sublist in xs for item in sublist)

        s = ''
        for key, value in flattened(self.buckets):
            s += repr(key) + ': ' + repr(value) + ', '
        return '{' + s + '}'

    __repr__ = __unicode__

    def __get_bucket(self, key):
        return self.buckets[hash(key) % len(self.buckets)]

    def put(self, key, value):
        bucket = self.__get_bucket(key)
        for item in bucket:
            if item[0] == key:
                item[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        """Avg complexity for a lookup with k buckets and n items:
            Number of collisions: min(0, n - k)
            Avg number of collisions per bucket: n / k
            -> O(n/k) search on average for each get()"""
        bucket = self.__get_bucket(key)
        for item in bucket:
            if item[0] == key:
                return item[1]
        return None
