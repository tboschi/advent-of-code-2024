""" Day 4 - part 1 """

from aoc.structures import Matrix


def read(path: str) -> list[str]:
    data = []
    with open(path) as file:
        for line in file:
            data.append(line.strip())
    return data


def search_dir(data: Matrix[str], rc: tuple[int, int], direction: tuple[int, int]) -> bool:
    r, c = rc
    dr, dc = direction
    for check in "MAS":
        r += dr
        c += dc
        if data[r, c] != check:
            return False
    return True


def search(data: Matrix[str], rc: tuple[int, int]) -> int:
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
    data = Matrix([list(p) for p in problem], "")
    tot = 0
    for rc, item in data:
        tot += search(data, rc)

    return tot


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
