""" Day 16 - part 2 """

import heapq
from collections import deque
from dataclasses import dataclass, field

from aoc.structures import Matrix

Point = tuple[int, int]


def add(p1: Point, p2: Point) -> Point:
    return p1[0] + p2[0], p1[1] + p2[1]


def find_neighbors(
    maze: Matrix[bool], node: Point, way: Point
) -> list[tuple[Point, Point]]:
    ffwd = way
    left = -way[1], -way[0]
    right = way[1], way[0]

    dirs = (ffwd, left, right)

    ns: list[tuple[Point, Point]] = []
    for new_way in dirs:
        new_pos = add(node, new_way)
        if not maze[new_pos]:
            continue
        ns.append((new_pos, new_way))

    return ns


def solve_maze(maze: Matrix[bool], start: Point, end: Point) -> int:
    visited: set[Point] = set()
    costs: dict[tuple[Point, Point], int] = {(start, (0, 1)): 0}
    steps: dict[tuple[Point, Point], int] = {(start, (0, 1)): 0}
    queue: list[tuple[int, Point, Point]] = [(0, start, (0, 1), 0)]

    while queue:
        cost, pos, way, step = heapq.heappop(queue)
        print("Check", pos, cost)

        if pos == end:
            return step

        if (pos, way) in visited:
            print("Already visited", pos, cost)
            continue

        visited.add((pos, way))

        for new_pos, new_way in find_neighbors(maze, pos, way):
            print("Add", new_pos)
            new_cost = cost + 1 + 1000 * (new_way != way)
            new_step = step + 1
            if new_cost < costs.get((new_pos, new_way), float("inf")):
                costs[(new_pos, new_way)] = new_cost
                steps[(new_pos, new_way)] = new_step
                heapq.heappush(queue, (new_cost, new_pos, new_way, new_step))

    return -1


def solve(problem: list[str]) -> int:
    maze = Matrix([[c != "#" for c in line] for line in problem], False)
    for r, line in enumerate(problem):
        if (c := line.find("S")) >= 0:
            start = r, c
        if (c := line.find("E")) >= 0:
            end = r, c

    print(start, end)

    return solve_maze(maze, start, end)


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

    example_alt = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""

    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
