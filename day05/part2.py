""" Day 5 - part 2 """

from functools import cmp_to_key

from aoc.structures import LabelTree
from aoc.utils import parse_list


def check_manual(rules: LabelTree, manual: list[int]) -> bool:
    prev, *manual = manual
    for page in manual:
        if page not in rules[prev]:
            return False
        prev = page
    return True


def fix_manual(rules: LabelTree, manual: list[int]) -> list[int]:
    return sorted(manual, key=cmp_to_key(rules.compare))


def solve(problem: list[str]) -> int:
    rules = LabelTree()
    manuals: list[list[int]] = []
    for line in problem:
        if "|" in line:
            before, _, after = line.partition("|")
            rules.add(int(before), int(after))
            continue

        if not line:
            continue

        manuals.append(parse_list(line))

    tot = 0
    for manual in manuals:
        if check_manual(rules, manual):
            continue

        fixed_manual = fix_manual(rules, manual)
        tot += fixed_manual[len(fixed_manual) // 2]

    return tot


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
