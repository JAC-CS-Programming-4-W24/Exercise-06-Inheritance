from typing import Generic, TypeVar, Iterator

from our_array import Array


class StackOverflowError(Exception):
    """Stack overflow error."""
    pass


class StackUnderflowError(Exception):
    """Stack underflow error."""
    pass


T = TypeVar("T")

class Stack(Generic[T]):
    """A last-in first-out (LIFO) collection of elements."""

    def __init__(self, capacity: int):
        self._elements: Array[T] = Array(capacity)
        self._tos: int = -1
        self._cursor: int

    def push(self, element: T):
        """
        Add an element on the top of the stack. Precondition: stack not full.
        :param element: The element to add to the stack.
        """
        if self.is_full():
            raise StackOverflowError()
        self._tos += 1
        self._elements[self._tos] = element

    def pop(self) -> T:
        """
        Remove the topmost element of the stack. Precondition: stack not empty.
        :return: The element removed from the stack.
        """
        if self.is_empty():
            raise StackUnderflowError()
        tmp: T = self._elements[self._tos]
        self._tos -= 1
        return tmp

    def top(self) -> T:
        """
        Get the topmost element of the stack. Precondition: stack not empty
        :return:
        """
        if self.is_empty():
            raise StackUnderflowError()
        return self._elements[self._tos]

    def is_empty(self) -> bool:
        """Determine if the stack is empty."""
        return self._tos == -1

    def is_full(self) -> bool:
        """Determine if the stack is full."""
        return self._tos == len(self._elements) - 1

    def __iter__(self) -> Iterator[T]:
        self._cursor = -1
        return self

    def __next__(self) -> T:
        if self._cursor == self._tos:
            raise StopIteration
        self._cursor += 1
        return self._elements[self._cursor]

    def __str__(self):
        if self.is_empty():
            return "[] <-- TOP"

        tmp: str = "["
        for i in range(self._tos):
            tmp += str(self._elements[i]) + ", "
        tmp += str(self._elements[self._tos])
        return tmp + "] <-- TOP"

    def __repr__(self):
        return str(self)
