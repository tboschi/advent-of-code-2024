""" Day 16 - part 1 """

from aoc.structures import Matrix
from dataclasses import dataclass

# import heapq
from collections import deque


Point = tuple[int, int]


@dataclass
class NodeInfo:
    way: Point
    steps: int = 0
    turns: int = 0

    @property
    def cost(self) -> int:
        return self.steps + 1000 * self.turns


def add(p1: Point, p2: Point) -> Point:
    return p1[0] + p2[0], p1[1] + p2[1]


def find_neighbors_ffwd(
    maze: Matrix[bool], pos: Point, info: NodeInfo, end: Point
) -> list[tuple[Point, NodeInfo]]:
    advance = True
    while advance:
        ffwd = info.way
        left = -info.way[1], -info.way[0]
        right = info.way[1], info.way[0]
        print("Advance", pos, ffwd, left, right)

        dirs = (ffwd, left, right)

        ns: list[tuple[Point, NodeInfo]] = []
        for new_way in dirs:
            new_pos = add(pos, new_way)
            if not maze[new_pos]:
                continue
            if new_pos == end:
                advance = False

            is_turn = info.way != new_way
            new_info = NodeInfo(new_way, info, info.steps + 1, info.turns + int(is_turn))
            ns.append((new_pos, new_info))

        if len(ns) != 1:
            advance = False
        else:
            pos, info = ns[0]

    print("Stop at", pos)
    return ns


def find_neighbors_ffwd(
    maze: Matrix[bool], pos: Point, info: NodeInfo, end: Point
) -> list[tuple[Point, NodeInfo]]:

    ffwd = info.way
    left = -info.way[1], -info.way[0]
    right = info.way[1], info.way[0]
    print("Advance", pos)

    dirs = (ffwd, left, right)

    ns: list[tuple[Point, NodeInfo]] = []
    for new_way in dirs:
        new_pos = add(pos, new_way)
        if not maze[new_pos]:
            continue

        is_turn = info.way != new_way
        new_info = NodeInfo(new_way, info.steps + 1, info.turns + int(is_turn))
        ns.append((new_pos, new_info))

    return ns


def solve_maze(maze: Matrix[bool], start: Point, end: Point) -> int:
    nodes: dict[Point, NodeInfo] = {start: NodeInfo((0, 1))}
    queue = deque(find_neighbors_ffwd(maze, start, nodes[start], end))

    while queue:
        pos, info = queue.pop()
        print("Check", pos, info)

        if pos == end:
            print("Found end", info.cost, (info.steps, info.turns))

        # Update cost if node was already visted
        if pos in nodes:
            print("Already visited", pos)
            if nodes[pos].cost > info.cost:
                nodes[pos] = info
            continue
        else:
            nodes[pos] = info

        # Node is at the end
        if pos == end:
            continue

        # Found end, node is more expensive and can be skipped
        if end in nodes:
            if info.cost > nodes[end].cost:
                print("Skip", pos)
                continue

        # It's a new node
        ns = find_neighbors_ffwd(maze, pos, info, end)
        print("Adding", ns)
        queue.extendleft(ns)

    return nodes[end].cost


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
    problem = read_from_string(example_alt)
    print(f"Example solution {solve(problem)}")
