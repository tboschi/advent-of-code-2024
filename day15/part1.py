""" Day 15 - part 1 """

from aoc.structures import Matrix

Point = tuple[int, int]

DIR = {"<" : (0, -1), "^" : (-1, 0), ">" : (0, 1), "v" : (1, 0)} 

def process_input(problem: list[str]) -> tuple[Matrix[str], str]:
    warehouse: list[str] = []
    instructions: list[str] = []
    for line in problem:
        if "#" in line:
            warehouse.append(line)
        else:
            instructions.append(line)
    return Matrix(warehouse, ""), "".join(instructions)

def move(pos: Point, direction: str) -> Point:
    d = DIR[direction]
    return pos[0] + d[0], pos[1] + d[1]

def find_wall(warehouse: Matrix[str], pos: Point, direction: str) -> Point:
    boxes = 0
    while warehouse[pos] != "#":
        boxes += warehouse[pos] == "O"
        pos = move(pos, direction)

def solve(problem: list[str]) -> int:
    warehouse, instructions = process_input(problem)

    for pos, item in warehouse:
        if item == "@":
            break
    warehouse[pos] = "."

    print("initial position", pos)
    for d in instructions:
        next_pos = move(pos, d)
        if warehouse[next_pos] == "#":
            continue

        wall, boxes = find_wall(warehouse, pos, d)

        if warehouse[next_pos] == ".":
            pos = next_pos
            continue
        assert warehouse[next_pos] == "O"

    return 0


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
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
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
