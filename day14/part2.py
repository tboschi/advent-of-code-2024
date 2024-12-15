""" Day 14 - part 2 """

import re
import math
import os
import time
from aoc.structures import Matrix

Pair = tuple[int, int]


class Robot:
    INFO = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

    def __init__(self, pos: Pair, vel: Pair) -> None:
        self.pos = pos
        self.vel = vel

    @classmethod
    def from_string(cls, info: str):
        m = cls.INFO.match(info)
        return Robot(
            (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))
        )

    def move(self, step: int = 1) -> None:
        x = (self.pos[0] + self.vel[0] * step) % 101
        y = (self.pos[1] + self.vel[1] * step) % 103
        self.pos = x, y


def autocorrelation(matrix: Matrix[int]) -> int:
    auto = 0
    for (r, c), item in matrix:
        auto += item * matrix[r, c - 1]
    return auto


def show(matrix: Matrix[int]) -> str:
    for r in range(matrix.rows):
        print(
            "".join(
                "O" if d else "."
                for d in matrix.data[r * matrix.cols : (r + 1) * matrix.cols]
            )
        )


def solve(problem: list[str]) -> int:
    robots: list[Robot] = []
    for line in problem:
        robots.append(Robot.from_string(line))

    for rob in robots:
        rob.move(7383)
    image = Matrix([[False] * 101 for _ in range(103)], False)
    for rob in robots:
        image[rob.pos] = True

    print(show(image))

    exit()

    step = 0
    max_correlation = 0
    while step < 7390:
        step += 1
        for rob in robots:
            rob.move()

        image = Matrix([[False] * 101 for _ in range(103)], False)
        for rob in robots:
            image[rob.pos] = True

        corr = autocorrelation(image)
        if corr > max_correlation:
            max_correlation = corr
            print(show(image))
        print(f"Step = {step} ->", corr)

    return 0


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
