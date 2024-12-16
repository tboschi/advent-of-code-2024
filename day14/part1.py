""" Day 14 - part 1 """

import math
import re

INFO = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

Pair = tuple[int, int]


def extract_info(robot: str) -> tuple[Pair, Pair]:
    m = INFO.match(robot)
    assert m is not None
    return (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))


def move_robot(pos: Pair, vel: Pair, shape: Pair, steps: int = 100) -> Pair:
    x = (pos[0] + vel[0] * steps) % shape[0]
    y = (pos[1] + vel[1] * steps) % shape[1]
    return x, y


def count_robots(robots: list[Pair], shape: Pair) -> int:
    counts = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}

    w, h = shape[0] // 2, shape[1] // 2
    for x, y in robots:
        if x == w or y == h:
            continue
        counts[(x > w, y > h)] += 1

    return math.prod(counts.values())


def solve(problem: list[str], shape: Pair = (101, 103)) -> int:
    final_pos: list[Pair] = []
    for line in problem:
        pos, vel = extract_info(line)
        pos = move_robot(pos, vel, shape, steps=100)
        final_pos.append(pos)

    return count_robots(final_pos, shape)


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem, (11,7))}")
