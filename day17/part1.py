""" Day 17 - part 1 """

import re

from aoc.utils import parse_list

R: dict[str, int] = {"A": 0, "B": 0, "C": 0, "P": 0}
OUT: list[int] = []


def combo(operand: int) -> int:
    match operand:
        case 4:
            return R["A"]
        case 5:
            return R["B"]
        case 6:
            return R["C"]
        case _:
            return operand


def movepointer() -> None:
    R["P"] += 2


def adv(operand: int) -> None:
    R["A"] = R["A"] // 2 ** combo(operand)
    movepointer()


def bdv(operand: int) -> None:
    R["B"] = R["A"] // 2 ** combo(operand)
    movepointer()


def cdv(operand: int) -> None:
    R["C"] = R["A"] // 2 ** combo(operand)
    movepointer()


def bxl(operand: int) -> None:
    R["B"] ^= operand
    movepointer()


def bst(operand: int) -> None:
    R["B"] = combo(operand) % 8
    movepointer()


def jnz(operand: int) -> None:
    if R["A"] != 0:
        R["P"] = operand
        return
    movepointer()


def bxc(operand: int) -> None:
    R["B"] = R["B"] ^ R["C"]
    movepointer()


def out(operand: int) -> None:
    OUT.append(combo(operand) % 8)
    movepointer()


def run(program: list[int]) -> None:
    while R["P"] < len(program):
        opcode = program[R["P"]]
        operand = program[R["P"] + 1]
        match opcode:
            case 0:
                adv(operand)
            case 1:
                bxl(operand)
            case 2:
                bst(operand)
            case 3:
                jnz(operand)
            case 4:
                bxc(operand)
            case 5:
                out(operand)
            case 6:
                bdv(operand)
            case 7:
                cdv(operand)


def solve(problem: list[str]) -> str:
    program: list[int]
    for line in problem:
        if m := re.match(r"Register ([ABC]): (\d+)", line):
            R[m.group(1)] = int(m.group(2))
        elif m := re.match(r"Program: ((\d,?)+)", line):
            program = parse_list(m.group(1))

    run(program)
    return ",".join(str(x) for x in OUT)


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
