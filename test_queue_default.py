import pytest

from our_queue import QueueOverflowError


class QueueDefault:
    pass  # TODO


@pytest.fixture
def queue() -> QueueDefault[str]:
    queue: QueueDefault[str] = QueueDefault(10, "foo")
    return queue


def test_queue_super_class_methods_still_work(queue):
    queue.enqueue("and")
    assert "and" == queue.dequeue()


def test_queue_enqueue_dequeue_with_default(queue):
    assert "foo" == queue.dequeue()
    queue.enqueue("def")
    assert "def" == queue.dequeue()
    assert "foo" == queue.dequeue()


def test_queue_is_empty(queue):
    # check that the queue is never empty
    queue.enqueue("abc")
    assert not queue.is_empty()
    queue.dequeue()
    assert not queue.is_empty()
    queue.dequeue()
    assert not queue.is_empty()


def test_queue_underflow(queue):
    # check that underflow is no longer a thing...
    for i in range(1000):
        queue.dequeue()


def test_queue_overflow_still_works(queue):
    with pytest.raises(QueueOverflowError):
        for i in range(11):
            queue.enqueue("def")
