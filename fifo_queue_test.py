import pytest
from fifo_queue import Queue, StackQueue, UnderflowException


def test_enqueue():
    q = Queue()
    assert q.is_empty
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert not q.is_empty
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.is_empty


def test_dequeue_empty_raises():
    with pytest.raises(UnderflowException):
        Queue().dequeue()


def test_stack_queue():
    q = StackQueue()
    assert q.is_empty
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert not q.is_empty
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.is_empty
