""" Day 7 - part 2 """

import math
from collections.abc import Sequence

from aoc.utils import parse_list


def cat(a: int, b: int) -> int:
    digits = int(math.log10(b)) + 1
    return a * 10**digits + b


def check(res: int, n0: int, ns: Sequence[int]) -> bool:
    if not ns:
        return res == n0

    return (
        check(res, n0 + ns[0], ns[1:])
        or check(res, n0 * ns[0], ns[1:])
        or check(res, cat(n0, ns[0]), ns[1:])
    )


def solve(problem: list[str]) -> int:
    tot = 0
    for line in problem:
        result, _, expression = line.partition(":")
        res = int(result)
        numbers = parse_list(expression, sep=None)
        if not numbers:
            continue

        if check(res, numbers[0], numbers[1:]):
            tot += res

    return tot


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
