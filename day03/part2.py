""" Day 3 - part 2 """

import re


def solve(problem: list[str]) -> int:
    mulop_regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    noop = re.compile(r"don't\(\).*?do\(\)")

    line = "".join(problem)
    line = noop.sub("", line)

    tot = 0
    for op in mulop_regex.finditer(line):
        if not op:
            continue
        tot += int(op[1]) * int(op[2])

    return tot


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
