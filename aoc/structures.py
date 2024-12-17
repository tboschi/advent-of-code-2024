""" Useful data structures """

from collections.abc import Iterator
from itertools import chain
from typing import Callable, Generic, TypeVar

T = TypeVar("T")


class Matrix(Generic[T]):
    """Easy access to 2D string data"""

    def __init__(self, data: list[list[T]], default: T):
        self.rows = len(data)
        self.cols = len(data[0])
        self.data = list(chain.from_iterable(data))
        self.default = default

    def __getitem__(self, rc: tuple[int, int]) -> T:
        r, c = rc
        if not (0 <= r < self.rows) or not (0 <= c < self.cols):
            return self.default
        return self.data[r * self.cols + c]

    def __setitem__(self, rc: tuple[int, int], value: T) -> None:
        r, c = rc
        if 0 <= r < self.rows and 0 <= c < self.cols:
            self.data[r * self.cols + c] = value

    def __iter__(self) -> Iterator[tuple[tuple[int, int], T]]:
        for rc, item in enumerate(self.data):
            yield divmod(rc, self.cols), item

    @property
    def shape(self) -> tuple[int, int]:
        return self.rows, self.cols


def show(matrix: Matrix[T], line_func: Callable) -> None:
    for r in range(matrix.rows):
        print(line_func(matrix.data[r * matrix.cols : (r + 1) * matrix.cols]))


class LabelTree:
    """Basic tree mapping integer nodes to each other"""

    def __init__(self) -> None:
        self.table: dict[int, set[int]] = {}

    def add(self, before: int, after: int) -> None:
        self.table.setdefault(before, set()).add(after)

    def __getitem__(self, key: int) -> set[int]:
        return self.table.get(key, set())

    def compare(self, page1: int, page2: int) -> int:
        if page1 in self[page2]:
            return 1
        if page2 in self[page1]:
            return -1
        return 0


class UnionFind(Generic[T]):
    def __init__(self, data: list[T] = []):
        self.root: dict[T, T] = {d: d for d in data}

    def __contains__(self, item: T) -> bool:
        return item in self.root

    def find(self, item: T) -> T:
        if item not in self:
            raise KeyError

        if self.root[item] == item:
            return item
        return self.find(self.root[item])

    def union(self, item1: T, item2: T) -> None:
        if item1 not in self.root:
            self.root[item1] = item1
        if item2 not in self.root:
            self.root[item2] = item2

        self.root[self.find(item1)] = self.find(item2)
