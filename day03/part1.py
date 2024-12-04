""" Day 3 - part 1 """

import re


def solve(problem: list[str]) -> int:
    reg = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    line = "".join(problem)

    tot = 0
    for op in reg.finditer(line):
        if not op:
            continue
        tot += int(op[1]) * int(op[2])

    return tot


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
