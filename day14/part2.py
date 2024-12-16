""" Day 14 - part 2 """

import math
import os
import re
import time
from typing import TypeVar, Type

from aoc.structures import Matrix

R = TypeVar("R", bound="Robot")

class Robot:
    INFO = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

    def __init__(self, pos: tuple[int, int], vel: tuple[int, int]) -> None:
        self.pos = pos
        self.vel = vel

    @classmethod
    def from_string(cls: Type[R], info: str) -> R:
        m = cls.INFO.match(info)
        assert m is not None
        return cls(
            (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))
        )

    def move(self, step: int = 1) -> None:
        x = (self.pos[0] + self.vel[0] * step) % 101
        y = (self.pos[1] + self.vel[1] * step) % 103
        self.pos = x, y


def autocorrelation(matrix: Matrix[bool]) -> int:
    """Autocorrelation on x with a lag of 1"""
    auto = 0
    for (r, c), item in matrix:
        auto += item * matrix[r, c - 1]
    return auto


def solve(problem: list[str]) -> int:
    robots: list[Robot] = []
    for line in problem:
        robots.append(Robot.from_string(line))

    step = 0
    max_correlation = 0
    max_correlation_step = 0
    while step < 10000:
        step += 1
        for rob in robots:
            rob.move()

        image = Matrix([[False] * 101 for _ in range(103)], False)
        for rob in robots:
            image[rob.pos] = True

        # Save step when correlation is high
        corr = autocorrelation(image)
        if corr > max_correlation:
            max_correlation = corr
            max_correlation_step = step

    return max_correlation_step


if __name__ == "__main__":
    pass
