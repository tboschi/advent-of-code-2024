import re

def read(path: str) -> list[str]:
    data = []
    with open(path) as file:
        for line in file:
            data.append(line.strip())
    return data

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
    import sys
    problem = read(sys.argv[1])
    print(solve(problem))
