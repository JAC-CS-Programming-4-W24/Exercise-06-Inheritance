from __future__ import annotations
from typing import Optional, Generic, TypeVar

"""
# Synopsis:

from array import Array, ArrayBoundsException

# create an integer array of size 4
arr: Array[int] = Array(4)
arr[0] = 123
arr[1] = 345
arr[2] = 456
arr[3] = 567

# create array of length 5 with three elements defined
b: Array[int] = Array(length=5, data=[1, 2, 3])

# print array
print(arr)  # prints [123, 345, 456, 567]

# loop over array
for x in arr:
    print(x)

# loop over array
for i in range(len(arr)):
    print(arr[i])

# error checking
try:
    arr[4] = 25
except ArrayBoundsException as e:
    print(e.args)


"""


class ArrayBoundsError(Exception):
    pass


T = TypeVar("T")


class Array(Generic[T]):
    """Mimics a classic array with generic type [T]"""
    access_counter: int = 0

    def __init__(self, length: int, data: list[T] = None):
        self.length: int = length
        self._cell: list[Optional[T]] = [None] * length
        if data is not None:
            for i in range(len(data)):
                self._cell[i] = data[i]

    def __check_array_bounds(self, index: int):
        if index < 0 or index >= self.length:
            raise ArrayBoundsError(f"Invalid index {index} for array of length {len(self._cell)}.")

    def __getitem__(self, index: int) -> Optional[T]:
        self.__check_array_bounds(index)
        Array.access_counter += 1
        return self._cell[index]

    def __setitem__(self, index: int, value: Optional[T]):
        self.__check_array_bounds(index)
        self._cell[index] = value

    def __delitem__(self, index: int):
        raise NotImplementedError

    def __str__(self) -> str:
        return "[" + ", ".join((str(v) if v is not None else " " for v in self._cell)) + "]"

    def __repr__(self):
        return repr(self._cell)

    def __len__(self):
        return len(self._cell)

    def __iter__(self):
        return iter(self._cell)


