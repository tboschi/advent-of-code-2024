from collections import Counter

from aoc.utils import read_test


def solve(problem: list[str]) -> int:
    list1: list[int] = []
    list2: list[int] = []
    for line in problem:
        if not line:
            continue
        l1, l2 = line.split()
        list1.append(int(l1))
        list2.append(int(l2))

    repeats = Counter(list2)
    return sum(l1 * repeats[l1] for l1 in list1)


if __name__ == "__main__":
    example = """
3   4
4   3
2   5
1   3
3   9
3   3
"""
    problem = read_test(example)
    print(f"Example solution {solve(problem)}")
