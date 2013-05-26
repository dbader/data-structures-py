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
