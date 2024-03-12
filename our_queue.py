from typing import Iterator, Generic, TypeVar

from our_array import Array

T = TypeVar("T")


class QueueOverflowError(Exception):
    """Queue overflow error."""
    pass


class QueueUnderflowError(Exception):
    """Queue underflow error."""
    pass


class Queue(Generic[T]):
    """A first-in first-out (FIFO) collection of elements. Optimized implementation using a "circular" array."""

    def __init__(self, capacity: int):
        self._elements: Array[T] = Array(capacity)
        self._front: int = 0
        self._rear: int = 0
        self._empty: bool = True

        # for traversals
        self._cursor: int
        self._first_step_taken: bool

    def enqueue(self, element: T):
        """
        Add an element on the rear of the queue. Precondition: queue not full.
        :param element: The element to add to the queue.
        """
        if self.is_full():
            raise QueueOverflowError()
        self._rear = (self._rear + 1) % len(self._elements)
        self._elements[self._rear] = element
        self._empty = False

    def dequeue(self) -> T:
        """
        Remove the front element of the queue. Precondition: queue not empty.
        :return: The element removed from the queue.
        """
        if self.is_empty():
            raise QueueUnderflowError()
        self._front = (self._front + 1) % len(self._elements)
        if self._front == self._rear:
            self._empty = True
        return self._elements[self._front]

    def front(self) -> T:
        """
        Get the front element of the queue. Precondition: queue not empty
        :return:
        """
        if self.is_empty():
            raise QueueUnderflowError()
        return self._elements[(self._front + 1) % len(self._elements)]

    def is_empty(self) -> bool:
        """Determine if the queue is empty."""
        return self._empty

    def is_full(self) -> bool:
        """Determine if the queue is full."""
        return self._rear == self._front and not self._empty

    def __iter__(self) -> Iterator[int]:
        self._cursor = self._front
        self._first_step_taken = False
        return self

    def __next__(self) -> T:
        if self._empty or (self._first_step_taken and self._cursor == self._rear):
            return StopIteration
        self._cursor = (self._cursor + 1) % len(self._elements)
        self._first_step_taken = True
        return self._elements[self._cursor]

    def __str__(self):
        if self._empty:
            return "FRONT --> [] <-- REAR"

        s: str = "FRONT --> ["
        i: int = (self._front + 1) % len(self._elements)
        while i != self._rear:
            s += str(self._elements[i]) + ", "
            i = (i + 1) % len(self._elements)
        s += str(self._elements[i])
        return s + "] <-- REAR"

    def __repr__(self):
        return str(self)
