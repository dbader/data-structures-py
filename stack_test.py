import pytest
from stack import Stack, UnderflowException


def test_push_pop():
    s = Stack()
    assert s.is_empty
    s.push(1)
    s.push(2)
    assert not s.is_empty
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty


def test_peek():
    s = Stack()
    s.push(1)
    assert s.peek() == 1
    assert s.pop() == 1


def test_underflow_throws():
    with pytest.raises(UnderflowException):
        Stack().pop()
