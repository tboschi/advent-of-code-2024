""" Day 17 - part 2 """

import re

from aoc.utils import parse_list

R = {"A": 0, "B": 0, "C": 0, "P": 0}
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
    global R
    R["P"] += 2


def adv(operand: int) -> None:
    global R
    R["A"] = R["A"] // 2 ** combo(operand)
    movepointer()


def bdv(operand: int) -> None:
    global R
    R["B"] = R["A"] // 2 ** combo(operand)
    movepointer()


def cdv(operand: int) -> None:
    global R
    R["C"] = R["A"] // 2 ** combo(operand)
    movepointer()


def bxl(operand: int) -> None:
    global R
    R["B"] ^= operand
    movepointer()


def bst(operand: int) -> None:
    global R
    R["B"] = combo(operand) % 8
    movepointer()


def jnz(operand: int) -> None:
    global R
    if R["A"] != 0:
        R["P"] = operand
        return
    movepointer()


def bxc(operand: int) -> None:
    global R
    R["B"] = R["B"] ^ R["C"]
    movepointer()


def out(operand: int) -> None:
    global OUT
    OUT.append(combo(operand) % 8)
    movepointer()


def run(program: list[int]) -> None:
    global R
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


def reverse_program(program: list[int], A: int, P: int) -> int:
    if P < 0:
        return A
    B = program[P]
    As = []
    for i in range(8):
        a = A * 8 + i
        b = ((i ^ 1) ^ 5) ^ (a // 2 ** (i ^ 1))
        if b % 8 == B:
            As.append(a)
    for A in As:
        guess = reverse_program(program, A, P - 1)
        if guess >= 0:
            return guess
    return -1


def solve(problem: list[str]) -> int:
    global R
    program: list[int]
    for line in problem:
        if m := re.match(r"Program: ((\d,?)+)", line):
            program = parse_list(m.group(1))

    A = reverse_program(program, 0, len(program) - 1)

    R = {"A": A, "B": 0, "C": 0, "P": 0}
    OUT.clear()
    run(program)
    print(",".join(str(x) for x in OUT))
    return A


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
Program: 0,3,5,4,3,0
"""

    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
