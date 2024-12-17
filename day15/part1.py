""" Day 15 - part 1 """

from aoc.structures import Matrix

Point = tuple[int, int]

DIR = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}


def process_input(problem: list[str]) -> tuple[Matrix[str], str]:
    warehouse: list[list[str]] = []
    instructions: list[str] = []
    for line in problem:
        if "#" in line:
            warehouse.append(list(line))
        else:
            instructions.append(line)
    return Matrix(warehouse, ""), "".join(instructions)


def move(pos: Point, direction: str) -> Point:
    d = DIR[direction]
    return pos[0] + d[0], pos[1] + d[1]


def move_boxes(warehouse: Matrix[str], pos: Point, direction: str) -> bool:
    p0 = pos
    while warehouse[pos] == "O":
        pos = move(pos, direction)

    if warehouse[pos] == "#":
        return False

    warehouse[p0] = "."
    warehouse[pos] = "O"
    return True


def calculate_gps(warehouse: Matrix[str]) -> int:
    tot = 0
    for (r, c), item in warehouse:
        if item == "O":
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
            case "O":
                if move_boxes(warehouse, next_pos, d):
                    pos = next_pos

    return calculate_gps(warehouse)


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example_small = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
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
