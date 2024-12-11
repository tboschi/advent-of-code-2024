""" Day 11 - part 1 """

import functools
import math

from aoc.utils import parse_list


@functools.cache
def expand(n: int, k: int):
    if k == 0:
        return 1
    k -= 1
    if n == 0:
        return expand(1, k)
    digits = int(math.log10(n)) + 1
    if digits % 2 == 1:
        return expand(2024 * n, k)
    digits //= 2
    left = n // 10**digits
    right = n - left * 10**digits
    return expand(left, k) + expand(right, k)


def solve(problem: list[str]) -> int:
    stones = parse_list(problem[0], sep=None)
    tot = 0
    for s in stones:
        tot += expand(s, 25)
    return tot


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
125 17
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
