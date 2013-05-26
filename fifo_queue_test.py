import pytest
from fifo_queue import Queue, UnderflowException


def test_enqueue():
    q = Queue()
    assert q.is_empty
    q.enqueue(1)
    q.enqueue(2)
    assert not q.is_empty
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.is_empty


def test_dequeue_empty_raises():
    with pytest.raises(UnderflowException):
        Queue().dequeue()
