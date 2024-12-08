""" Day 6 - part 1 """

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


def solve(problem: list[str]) -> int:
    area = Matrix([list(p) for p in problem])
    positions = set()
    for pos, cur in area:
        if cur in ("<", "^", ">", "v"):
            break

    area[pos] = "."

    move = DIRECTIONS[cur]
    while tile := area[pos]:
        if tile == ".":
            positions.add(pos)
            pos = advance(pos, move)
        elif tile == "#":
            pos = retreat(pos, move)
            cur = next_direction(cur)
            move = DIRECTIONS[cur]
    return len(positions)


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
