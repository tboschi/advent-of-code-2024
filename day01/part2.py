import re
from collections import Counter

def read(path: str) -> list[str]:
    data = []
    with open(path) as file:
        for line in file:
            data.append(line.strip())
    return data

def solve(problem: list[str]) -> int:
    list1: list[str] = []
    list2: list[str] = []
    for line in problem:
        match = re.match("(\d+)\s+(\d+)", line)
        if match is None:
            continue
        list1.append(int(match[1]))
        list2.append(int(match[2]))

    repeats = Counter(list2)
    return sum(l1 * repeats[l1] for l1 in list1)


if __name__ == "__main__":
    import sys
    problem = read(sys.argv[1])
    print(solve(problem))
