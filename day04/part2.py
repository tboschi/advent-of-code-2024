""" Day 4 - part 1 """

from aoc.structures import Matrix


def read(path: str) -> list[str]:
    data = []
    with open(path) as file:
        for line in file:
            data.append(line.strip())
    return data


def search_mas(data: Matrix[str], rc: tuple[int, int], direction: bool) -> bool:
    r, c = rc
    if direction:
        corners = data[r - 1, c - 1], data[r + 1, c + 1]
    else:
        corners = data[r - 1, c + 1], data[r + 1, c - 1]
    return corners == ("M", "S") or corners == ("S", "M")


def search(data: Matrix[str], rc: tuple[int, int]) -> bool:
    if data[rc] != "A":
        return False

    return search_mas(data, rc, False) and search_mas(data, rc, True)


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
