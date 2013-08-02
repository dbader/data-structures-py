class BitSet:
    def __init__(self, bits=0x00):
        self.bits = bits

    def set(self, i):
        self.bits |= (1 << i)

    def clear(self, i):
        self.bits ^= (1 << i)

    def test(self, i):
        return self.bits & (1 << i) != 0

    def negation(self):
        return BitSet(0xFF ^ self.bits)

    def union(self, other):
        return BitSet(self.bits | other.bits)

    def intersection(self, other):
        return BitSet(self.bits & other.bits)

    def subtract(self, other):
        return BitSet(self.bits ^ other.bits)
