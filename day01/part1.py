import re

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

    list1.sort()
    list2.sort()

    return sum(abs(l1 - l2) for l1, l2 in zip(list1, list2))


if __name__ == "__main__":
    import sys
    problem = read(sys.argv[1])
    print(solve(problem))
