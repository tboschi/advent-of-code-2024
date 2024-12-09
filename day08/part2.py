""" Day 8 - part 2 """

import itertools

from aoc.structures import Matrix


def find_antinodes(
    antennas: list[tuple[int, int]], bounds: tuple[int, int]
) -> list[tuple[int, int]]:
    antinodes: set[tuple[int, int]] = set()

    for p1, p2 in itertools.combinations(antennas, 2):
        delta = p1[0] - p2[0], p1[1] - p2[1]

        while 0 <= p1[0] < bounds[0] and 0 <= p1[1] < bounds[1]:
            antinodes.add(p1)
            p1 = p1[0] + delta[0], p1[1] + delta[1]

        while 0 <= p2[0] < bounds[0] and 0 <= p2[1] < bounds[1]:
            antinodes.add(p2)
            p2 = p2[0] - delta[0], p2[1] - delta[1]

    return list(antinodes)


def solve(problem: list[str]) -> int:
    area = Matrix([list(p) for p in problem], "")
    shadow = Matrix([[False] * area.cols for _ in range(area.rows)], False)

    antennas: dict[str, list[tuple[int, int]]] = {}
    for rc, antenna in area:
        if antenna != ".":
            antennas.setdefault(antenna, []).append(rc)

    for ant, pos in antennas.items():
        antis = find_antinodes(pos, area.shape)
        for rc in antis:
            shadow[rc] = True

    tot = 0
    for _, val in shadow:
        tot += val

    return tot


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
