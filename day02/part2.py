def read(path: str) -> list[str]:
    data = []
    with open(path) as file:
        for line in file:
            data.append(line.strip())
    return data

def compare_levels(cmp: int, ref: bool) -> bool:
    if cmp == 0:
        return False
    if abs(cmp) > 3:
        return False
    return (cmp > 0) == ref

def is_report_safe(report: list[int]) -> bool:
    cur, *report = report
    ref = None
    skip1 = False
    for lev in report:
        cmp = lev - cur
        if ref is None:
            ref = cmp > 0
        if not compare_levels(cmp, ref):
            if skip1:
                return False
            skip1 = True
            print(f"skip {cur}, {lev}")
            continue
        cur = lev
    return True

def solve(problem: list[str]) -> int:
    tot = 0
    for line in problem:
        report = [int(l) for l in line.split()]
        if not report:
            continue
        ok = is_report_safe(report)
        print(report, ok)
        tot += ok

    return tot


if __name__ == "__main__":
    import sys
    problem = read(sys.argv[1])
    print(solve(problem))
