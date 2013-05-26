from vector import Vector


def test_instantiate():
    assert Vector() is not None


def test_append():
    v = Vector()
    for x in range(1000):
        v.append(x)
        assert v[x] == x
    assert v.length == 1000


def test_set_item():
    v = Vector()
    for x in range(100):
        v.append(x)
    v[0] = 991
    v[20] = 992
    v[40] = 993
    v[99] = 994
    assert v[0] == 991
    assert v[20] == 992
    assert v[40] == 993
    assert v[99] == 994


def test_delete():
    v = Vector()
    v.append(1)
    v.append(2)
    v.append(3)
    assert v.length == 3
    v.delete(1)
    assert v.length == 2
    assert v[0] == 1
    assert v[1] == 3


def test_delete_many():
    v = Vector()
    for x in range(1000):
        v.append(x)
    c = v.capacity
    for x in range(1000):
        v.delete(v.length // 2)
    assert v.capacity < c
    assert v.length == 0
