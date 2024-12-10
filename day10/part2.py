""" Day 10 - part 2 """

from aoc.structures import Matrix

Point = tuple[int, int]

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)


def move(pos: Point, n: Point) -> Point:
    return pos[0] + n[0], pos[1] + n[1]


def explore_n(area: Matrix[int], pos: Point, n: Point) -> int:
    adj = move(pos, n)
    if adj == pos or area[adj] != area[pos] + 1:
        return 0
    return explore(area, adj)


def explore(area: Matrix[int], pos: Point, n: int | None = None) -> int:
    if area[pos] == 9:
        return 1

    return (
        explore_n(area, pos, N)
        + explore_n(area, pos, E)
        + explore_n(area, pos, S)
        + explore_n(area, pos, W)
    )


def solve(problem: list[str]) -> int:
    area = Matrix([[int(c) for c in line] for line in problem], -1)

    tot = 0
    for rc, head in area:
        if head == 0:
            peaks = explore(area, rc)
            tot += peaks

    return tot


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
