""" Day 13 - part 1 """

import re
from typing import cast

BUTTON = re.compile(r"Button \w: X\+(\d+), Y\+(\d+)")
PRIZE = re.compile(r"Prize: X=(\d+), Y=(\d+)")

Pair = tuple[int, int]


def extract_info(
    machine: list[str],
) -> tuple[Pair, Pair, Pair]:
    A = BUTTON.match(machine[0])
    B = BUTTON.match(machine[1])
    P = PRIZE.match(machine[2])

    to_int = lambda x: (int(x.group(1)), int(x.group(2)))
    return to_int(A), to_int(B), to_int(P)


def solve_equation(A: Pair, B: Pair, P: Pair) -> Pair | None:
    det = A[0] * B[1] - A[1] * B[0]
    pa = P[0] * B[1] - P[1] * B[0]
    pb = P[1] * A[0] - P[0] * A[1]
    na, ra = divmod(pa, det)
    nb, rb = divmod(pb, det)

    if ra != 0 or rb != 0:
        return None
    return na, nb


def solve(problem: list[str]) -> int:
    tot = 0
    for batch in range(0, len(problem), 3):
        A, B, P = extract_info(problem[batch : batch + 3])
        res = solve_equation(A, B, P)
        if res is None:
            continue
        tot += 3 * res[0] + res[1]
    return tot


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
