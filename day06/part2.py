""" Day 6 - part 2 """

from collections.abc import Callable

from aoc.structures import Matrix

DIRECTIONS: dict[str, tuple[int, int]] = {
    "<": (0, -1),
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
}


def next_direction(current_dir: str) -> str:
    directions = list(DIRECTIONS)
    index = directions.index(current_dir)
    return directions[(index + 1) % len(directions)]


def advance(pos: tuple[int, int], move: tuple[int, int]) -> tuple[int, int]:
    return pos[0] + move[0], pos[1] + move[1]


def retreat(pos: tuple[int, int], move: tuple[int, int]) -> tuple[int, int]:
    return pos[0] - move[0], pos[1] - move[1]


def possible_positions(
    area: Matrix, pos: tuple[int, int], cur: str
) -> set[tuple[int, int]]:
    positions: set[tuple[int, int]] = set()
    delta = DIRECTIONS[cur]
    while tile := area[pos]:
        if tile == "#":
            pos = retreat(pos, delta)
            cur = next_direction(cur)
            delta = DIRECTIONS[cur]
            continue

        assert tile == "."

        positions.add(pos)
        pos = advance(pos, delta)
    return positions


def detect_loop(area: Matrix, pos: tuple[int, int], cur: str) -> bool:
    positions: set[tuple[str, int, int]] = set()
    delta = DIRECTIONS[cur]
    while tile := area[pos]:
        if tile == "#":
            pos = retreat(pos, delta)
            cur = next_direction(cur)
            delta = DIRECTIONS[cur]
            continue

        assert tile == "."
        if (cur, *pos) in positions:
            return True

        positions.add((cur, *pos))
        pos = advance(pos, delta)

    return False


def solve(problem: list[str]) -> int:
    area = Matrix([list(p) for p in problem])
    positions: set[tuple[int, int]] = set()
    for p0, c0 in area:
        if c0 in DIRECTIONS:
            break
    area[p0] = "."

    positions = possible_positions(area, p0, c0)

    tot = 0
    for pos in positions:
        if pos == p0:
            continue

        area[pos] = "#"
        if detect_loop(area, p0, c0):
            tot += 1
        area[pos] = "."

    return tot


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
