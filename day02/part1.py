""" Day 2 - part 1 """


def compare_levels(cmp: int, ref: bool) -> bool:
    if cmp == 0:
        return False
    if abs(cmp) > 3:
        return False
    return (cmp > 0) == ref


def is_report_safe(report: list[int]) -> bool:
    cur, *report = report
    ref = None
    for lev in report:
        cmp = lev - cur
        if ref is None:
            ref = cmp > 0
        if not compare_levels(cmp, ref):
            return False
        cur = lev
    return True


def solve(problem: list[str]) -> int:
    tot = 0
    for line in problem:
        report = [int(l) for l in line.split()]
        tot += is_report_safe(report)

    return tot


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
