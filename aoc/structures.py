""" Useful data structures """

from collections.abc import Iterator
from itertools import chain


class Matrix:
    """Easy access to 2D string data"""

    def __init__(self, data: list[list[str]], default: str = ""):
        self.rows = len(data)
        self.cols = len(data[0])
        self.data = list(chain.from_iterable(data))
        self.default = default

    def __getitem__(self, rc: tuple[int, int]) -> str:
        r, c = rc
        if not (0 <= r < self.rows) or not (0 <= c < self.cols):
            return self.default
        return self.data[r * self.cols + c]

    def __setitem__(self, rc: tuple[int, int], value: str) -> None:
        r, c = rc
        if 0 < r <= self.rows and 0 < c <= self.cols:
            self.data[r * self.cols + c] = value

    def __iter__(self) -> Iterator[tuple[tuple[int, int], str]]:
        for rc, item in enumerate(self.data):
            yield divmod(rc, self.cols), item


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
