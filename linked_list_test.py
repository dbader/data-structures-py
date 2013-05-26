from linked_list import LinkedList


def test_head():
    assert LinkedList(1, 2, 3, 4).head == 1


def test_tail():
    assert LinkedList(1, 2, 3, 4).tail == LinkedList(2, 3, 4)


def test_is_empty():
    assert LinkedList().is_empty
    assert not LinkedList('a', 'b', 'c').is_empty


def test_length():
    assert LinkedList().length == 0
    assert LinkedList(1, 2, 3, 4, 5).length == 5
    assert len(LinkedList(1, 2, 3, 4, 5)) == 5


def test_to_string():
    assert str(LinkedList()) == '[]'
    assert str(LinkedList(1, 2, 3)) == '[1, 2, 3]'


def test_prepend():
    assert LinkedList(2, 3).prepend(1) == LinkedList(1, 2, 3)


def test_append():
    assert LinkedList().append(1) == LinkedList(1)
    assert LinkedList(1, 2).append(3) == LinkedList(1, 2, 3)


def test_concatenate():
    assert LinkedList().concat(LinkedList()) == LinkedList()
    assert LinkedList().concat(LinkedList(1)) == LinkedList(1)
    assert LinkedList(1).concat(LinkedList(2)) == LinkedList(1, 2)
    assert LinkedList(1, 2).concat(LinkedList(3, 4)) == LinkedList(1, 2, 3, 4)


def test_take():
    assert LinkedList(1, 2, 3, 4).take(2) == LinkedList(1, 2)


def test_drop():
    assert LinkedList(1, 2, 3).drop(1) == LinkedList(2, 3)
    assert LinkedList(1, 2, 3, 4).drop(2) == LinkedList(3, 4)


def test_indexing():
    assert LinkedList(1, 2, 3)[0] == 1
    assert LinkedList(1, 2, 3)[2] == 3


def test_iteration():
    l = LinkedList(0, 1, 2, 3)
    for i, x in enumerate(l):
        assert i == x


def test_allows_none_as_element():
    assert LinkedList().prepend(None).head == None
    assert LinkedList(1, 2, None, 3).drop(2).tail == LinkedList(3)
