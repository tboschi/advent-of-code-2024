from collections.abc import Iterator


def read(path: str) -> list[str]:
    data = []
    with open(path) as file:
        for line in file:
            data.append(line.strip())
    return data


class Matrix:
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


def search_dir(data: Matrix, rc: tuple[int], direction: tuple[int, int]) -> bool:
    r, c = rc
    dr, dc = direction
    for check in "MAS":
        r += dr
        c += dc
        if data[r, c] != check:
            return False
    return True


def search(data: Matrix, rc: tuple[int]) -> int:
    if data[rc] != "X":
        return 0

    return sum(
        search_dir(data, rc, direction)
        for direction in [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
    )


def solve(problem: list[str]) -> int:
    data = Matrix(problem)
    tot = 0
    for rc, item in data:
        tot += search(data, rc)

    return tot


if __name__ == "__main__":
    import sys

    problem = read(sys.argv[1])
    print(solve(problem))
