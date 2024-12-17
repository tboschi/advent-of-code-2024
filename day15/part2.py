""" Day 15 - part 2 """

from collections import deque

from aoc.structures import Matrix

Point = tuple[int, int]

DIR = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}


def process_input(problem: list[str]) -> tuple[Matrix[str], str]:
    warehouse: list[list[str]] = []
    instructions: list[str] = []
    for line in problem:
        if "#" in line:
            line = line.replace("#", "##")
            line = line.replace("O", "[]")
            line = line.replace(".", "..")
            line = line.replace("@", "@.")
            warehouse.append(list(line))
        else:
            instructions.append(line)
    return Matrix(warehouse, ""), "".join(instructions)


def move(pos: Point, direction: str, step: int = 1) -> Point:
    d = DIR[direction]
    return pos[0] + step * d[0], pos[1] + step * d[1]


def move_boxes_lr(warehouse: Matrix[str], pos: Point, direction: str) -> bool:
    p0 = pos
    stack: dict[Point, str] = {}
    while warehouse[pos] in ("[", "]"):
        stack[pos] = warehouse[pos]
        pos = move(pos, direction)

    if warehouse[pos] == "#":
        return False

    for pos in stack:
        warehouse[pos] = "."
    for pos, val in stack.items():
        warehouse[move(pos, direction)] = val
    return True


def move_boxes_tb(warehouse: Matrix[str], pos: Point, direction: str) -> bool:
    p0 = pos
    queue: deque[Point] = deque([p0])
    stack: dict[Point, str] = {}
    while queue:
        pos = queue.pop()
        if warehouse[pos] not in ("[", "]"):
            continue
        stack[pos] = warehouse[pos]

        # look forward first
        next_pos = move(pos, direction)
        val = warehouse[next_pos]
        if val == "#":
            return False
        if val != "." and next_pos not in stack:
            queue.appendleft(next_pos)

        # look left or right
        val = warehouse[pos]
        if val == "[":
            next_pos = move(pos, ">")
            if next_pos not in stack:
                queue.appendleft(next_pos)
        elif val == "]":
            next_pos = move(pos, "<")
            if next_pos not in stack:
                queue.appendleft(next_pos)

    for pos in stack:
        warehouse[pos] = "."
    for pos, val in stack.items():
        warehouse[move(pos, direction)] = val
    return True


def move_boxes(warehouse: Matrix[str], pos: Point, direction: str) -> bool:
    return (
        move_boxes_lr(warehouse, pos, direction)
        if direction in ("<", ">")
        else move_boxes_tb(warehouse, pos, direction)
    )


def calculate_gps(warehouse: Matrix[str]) -> int:
    tot = 0
    for (r, c), item in warehouse:
        if item == "[":
            tot += 100 * r + c

    return tot


def solve(problem: list[str]) -> int:
    warehouse, instructions = process_input(problem)

    for pos, item in warehouse:
        if item == "@":
            break
    warehouse[pos] = "."

    for d in instructions:
        next_pos = move(pos, d)
        match warehouse[next_pos]:
            case "#":
                continue
            case ".":
                pos = next_pos
            case "[" | "]":
                if move_boxes(warehouse, next_pos, d):
                    pos = next_pos

    return calculate_gps(warehouse)


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example_small = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""

    example = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
