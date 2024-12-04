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

def search_mas(data: Matrix, rc: tuple[int], direction: bool) -> bool:
    r, c = rc
    if direction:
        corners = data[r - 1, c - 1], data[r + 1, c + 1]
    else:
        corners = data[r - 1, c + 1], data[r + 1, c - 1]
    return corners == ("M", "S") or corners == ("S", "M")


def search(data: Matrix, rc: tuple[int]) -> bool:
    if data[rc] != "A":
        return False

    return search_mas(data, rc, False) and search_mas(data, rc, True)


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
