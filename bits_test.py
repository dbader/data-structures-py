from bits import *


def test_bitset():
    s = BitSet()
    assert not s.test(3)
    s.set(3)
    assert s.test(3)
    assert not s.test(0)
    assert not s.test(1)
    assert not s.test(2)
    assert not s.test(4)
    assert not s.test(5)
    assert not s.test(6)
    assert not s.test(7)
    s.clear(3)
    assert not s.test(3)


def test_negation():
    a = BitSet()
    a.set(4)
    assert a.test(4)
    assert not a.test(0)
    assert not a.test(7)

    a = a.negation()

    assert not a.test(4)
    assert a.test(0)
    assert a.test(7)


def test_union():
    a = BitSet()
    b = BitSet()
    a.set(2)
    b.set(5)
    c = a.union(b)
    assert c.test(2)
    assert c.test(5)


def test_intersection():
    a = BitSet()
    b = BitSet()
    a.set(2)
    a.set(3)
    b.set(5)
    b.set(3)
    c = a.intersection(b)
    assert not c.test(2)
    assert c.test(3)
    assert not c.test(5)


def test_subtraction():
    a = BitSet()
    b = BitSet()
    a.set(2)
    a.set(3)
    b.set(5)
    b.set(3)
    c = a.subtract(b)
    assert c.test(2)
    assert not c.test(3)
