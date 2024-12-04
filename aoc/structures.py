""" Useful data structures """

from collections.abc import Iterator


class Matrix:
    """Easy access to 2D data"""

    def __init__(self, problem: list[str], default: str = ""):
        self.rows = len(problem)
        self.cols = len(problem[0])
        self.data = "".join(problem)
        self.default = default

    def __getitem__(self, rc: tuple[int, int]) -> str:
        r, c = rc
        if r < 0 or r >= self.rows:
            return self.default
        if c < 0 or c >= self.cols:
            return self.default
        return self.data[r * self.cols + c]

    def __iter__(self) -> Iterator[tuple[tuple[int, int], str]]:
        for rc, item in enumerate(self.data):
            yield divmod(rc, self.cols), item
