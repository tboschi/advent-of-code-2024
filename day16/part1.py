""" Day 16 - part 1 """

import heapq
from collections import deque
from dataclasses import dataclass, field

from aoc.structures import Matrix

Point = tuple[int, int]
Node = tuple[Point, Point]


def add(p1: Point, p2: Point) -> Point:
    return p1[0] + p2[0], p1[1] + p2[1]


class Node:
    def __init__(self, pos, way):
        self.pos = pos
        self.way = way

    def __lt__(self, other):
        return self.data < other.data

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self) -> str:
        return str(self.data)

    @property
    def data(self):
        return self.pos, self.way


def find_neighbors(maze: Matrix[bool], node: Node) -> list[Node]:
    ffwd = node.way
    left = -ffwd[1], -ffwd[0]
    right = ffwd[1],  ffwd[0]

    dirs = (ffwd, left, right)

    ns: list[Node] = []
    for new_way in dirs:
        new_pos = add(node.pos, new_way)
        if not maze[new_pos]:
            continue
        new_node = Node(new_pos, new_way)
        ns.append(new_node)

    return ns


def solve_maze(maze: Matrix[bool], start: Point, end: Point) -> int:
    start_node = Node(start, (0, 1))
    costs: dict[Node, int] = {start_node: 0}
    queue: list[tuple[int, Node]] = [(0, start_node)]
    visited: set[Node] = set()

    while queue:
        cost, node = heapq.heappop(queue)

        if node.pos == end:
            break

        if node in visited:
            continue

        visited.add(node)

        for new_node in find_neighbors(maze, node):
            new_cost = cost + 1 + 1000 * (new_node.way != node.way)
            if new_cost < costs.get(new_node, float("inf")):
                costs[new_node] = new_cost
                heapq.heappush(queue, (new_cost, new_node))

    return cost 


def solve(problem: list[str]) -> int:
    maze = Matrix([[c != "#" for c in line] for line in problem], False)
    for r, line in enumerate(problem):
        if (c := line.find("S")) >= 0:
            start = r, c
        if (c := line.find("E")) >= 0:
            end = r, c

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

    problem = read_from_string(example_alt)
    print(f"Example solution {solve(problem)}")
